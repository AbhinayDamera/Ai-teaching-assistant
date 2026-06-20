import React, { useState, useRef, useEffect } from 'react';
import { motion } from 'framer-motion';
import { ArrowLeft, Mic, Send, Volume2, Loader } from 'lucide-react';
import axios from 'axios';
import './ExplainMode.css';

const API_URL = process.env.REACT_APP_API_URL || '';

const ExplainMode = ({ onBack }) => {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [isListening, setIsListening] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const recognitionRef = useRef(null);

  // Load voices when component mounts
  useEffect(() => {
    // Load voices (needed for some browsers)
    if (window.speechSynthesis) {
      window.speechSynthesis.getVoices();
      window.speechSynthesis.onvoiceschanged = () => {
        window.speechSynthesis.getVoices();
      };
    }

    // Initialize Speech Recognition
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = false;
      recognitionRef.current.interimResults = false;
      recognitionRef.current.lang = 'hi-IN'; // Hindi

      recognitionRef.current.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        setQuestion(transcript);
        setIsListening(false);
      };

      recognitionRef.current.onerror = (event) => {
        console.error('Speech recognition error:', event.error);
        setIsListening(false);
        if (event.error === 'no-speech') {
          alert('No speech detected. Please try again.');
        } else if (event.error === 'not-allowed') {
          alert('Microphone access denied. Please allow microphone permissions.');
        } else {
          alert('Could not recognize speech. Please try again.');
        }
      };

      recognitionRef.current.onend = () => {
        setIsListening(false);
      };
    }
  }, []);

  const handleAsk = async () => {
    if (!question.trim()) return;

    setIsLoading(true);
    setAnswer('');

    try {
      const response = await axios.post(`${API_URL}/api/explain`, { question });
      const explanation = response.data.explanation;
      setAnswer(explanation);
      setHistory([{ question, answer: explanation }, ...history]);
    } catch (error) {
      setAnswer('❌ Error: Could not get explanation. Check backend connection.');
    } finally {
      setIsLoading(false);
    }
  };

  const playAudio = (text) => {
    try {
      // Stop any ongoing speech
      window.speechSynthesis.cancel();
      
      // Create speech utterance
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'hi-IN'; // Hindi language
      utterance.rate = 0.9; // Slightly slower for clarity
      utterance.pitch = 1;
      utterance.volume = 1;
      
      // Try to find a Hindi voice
      const voices = window.speechSynthesis.getVoices();
      const hindiVoice = voices.find(voice => voice.lang.includes('hi')) || 
                         voices.find(voice => voice.lang.includes('en-IN'));
      
      if (hindiVoice) {
        utterance.voice = hindiVoice;
      }
      
      window.speechSynthesis.speak(utterance);
    } catch (error) {
      console.error('TTS error:', error);
      alert('Could not play audio. Please check browser permissions.');
    }
  };

  const toggleRecording = () => {
    if (!recognitionRef.current) {
      alert('Speech recognition not supported in this browser. Please use Chrome.');
      return;
    }

    if (isListening) {
      recognitionRef.current.stop();
      setIsListening(false);
    } else {
      try {
        recognitionRef.current.start();
        setIsListening(true);
      } catch (error) {
        console.error('Error starting recognition:', error);
        alert('Could not start recording. Please try again.');
      }
    }
  };

  return (
    <motion.div
      className="container"
      initial={{ opacity: 0, x: 100 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -100 }}
      transition={{ duration: 0.5 }}
    >
      <div className="page">
        <button className="back-button" onClick={onBack}>
          <ArrowLeft size={20} /> Back to Home | होम पर वापस जाएं
        </button>

        <div className="header">
          <h1>🧠 Explain Concept | अवधारणा समझाएं</h1>
          <p className="subtitle">Ask any question in Hindi, English, or Hinglish</p>
          <p className="subtitle">हिंदी, अंग्रेज़ी या हिंग्लिश में कोई भी सवाल पूछें</p>
        </div>

        <div className="input-section">
          <input
            type="text"
            placeholder="Type your question... | अपना सवाल लिखें... (या माइक बटन दबाएं)"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleAsk()}
            className="question-input"
          />
          <div className="button-group">
            <motion.button
              className={`mic-button ${isListening ? 'listening' : ''}`}
              onClick={toggleRecording}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <Mic size={24} />
              {isListening ? '🔴 Recording... | रिकॉर्ड हो रहा है... (Click to Stop | बंद करने के लिए क्लिक करें)' : '🎤 Click to Speak | बोलने के लिए क्लिक करें'}
            </motion.button>
            <motion.button
              className="send-button"
              onClick={handleAsk}
              disabled={isLoading}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {isLoading ? <Loader className="spin" size={24} /> : <Send size={24} />}
              Ask | पूछें
            </motion.button>
          </div>
        </div>

        {answer && (
          <motion.div
            className="answer-box"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <div className="answer-header">
              <h3>📝 Answer | उत्तर:</h3>
              <button className="speak-button" onClick={() => playAudio(answer)}>
                <Volume2 size={20} /> Speak | सुनें
              </button>
            </div>
            <div className="answer-content">
              {answer.split('\n').map((line, i) => (
                <p key={i} className={
                  line.startsWith('🇬🇧') ? 'lang-header english-header' :
                  line.startsWith('🇮🇳') ? 'lang-header hindi-header' :
                  line.startsWith('💡') ? 'tip-line' : 'answer-line'
                }>
                  {line}
                </p>
              ))}
            </div>
          </motion.div>
        )}

        {history.length > 0 && (
          <div className="history-section">
            <h3>📜 Recent Questions | हाल के सवाल</h3>
            {history.slice(0, 3).map((item, index) => (
              <motion.div
                key={index}
                className="history-item"
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
              >
                <strong>Q:</strong> {item.question}
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </motion.div>
  );
};

export default ExplainMode;
