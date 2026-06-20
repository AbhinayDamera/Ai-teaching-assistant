import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ArrowLeft, Mic, Send, CheckCircle, XCircle, Trophy, Loader } from 'lucide-react';
import axios from 'axios';
import './QuizMode.css';

const API_URL = process.env.REACT_APP_API_URL || '';

const QuizMode = ({ onBack }) => {
  const [topic, setTopic] = useState('');
  const [quiz, setQuiz] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState(null);
  const [showResult, setShowResult] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  const generateQuiz = async () => {
    if (!topic.trim()) return;

    setIsLoading(true);
    try {
      const response = await axios.post(`${API_URL}/api/quiz/generate`, { topic, num_questions: 5 });
      setQuiz(response.data);
      setCurrentQuestion(0);
      setScore(0);
      setSelectedAnswer(null);
      setShowResult(false);
    } catch (error) {
      alert('❌ Could not generate quiz. Check backend connection.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleAnswer = (index) => {
    if (selectedAnswer !== null) return; // Already answered

    setSelectedAnswer(index);
    const correct = quiz.questions[currentQuestion].correct;

    if (index === correct) {
      setScore(score + 1);
    }
  };

  const handleNextQuestion = () => {
    if (currentQuestion < quiz.questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setSelectedAnswer(null);
    } else {
      setShowResult(true);
    }
  };

  const resetQuiz = () => {
    setQuiz(null);
    setTopic('');
    setCurrentQuestion(0);
    setScore(0);
    setSelectedAnswer(null);
    setShowResult(false);
  };

  if (showResult) {
    const percentage = (score / quiz.questions.length) * 100;

    return (
      <motion.div
        className="container"
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.8 }}
      >
        <div className="page result-page">
          <Trophy size={100} color="#ffd700" />
          <h1>🎉 Quiz Complete! | क्विज़ पूरा हुआ!</h1>
          <div className="score-display">
            <h2>{score} / {quiz.questions.length}</h2>
            <p>{percentage.toFixed(0)}%</p>
          </div>
          <p className="result-message">
            {percentage >= 80 && "🌟 Bahut badhiya! Excellent performance! | बहुत बढ़िया! शानदार प्रदर्शन!"}
            {percentage >= 60 && percentage < 80 && "👍 Accha hai! Keep practicing! | अच्छा है! अभ्यास जारी रखें!"}
            {percentage < 60 && "💪 Koi baat nahi! Practice more and try again! | कोई बात नहीं! और अभ्यास करें!"}
          </p>
          <div className="result-buttons">
            <button className="button-primary" onClick={resetQuiz}>
              🔄 New Quiz | नई क्विज़
            </button>
            <button className="button-secondary" onClick={onBack}>
              🏠 Home | होम
            </button>
          </div>
        </div>
      </motion.div>
    );
  }

  if (!quiz) {
    return (
      <motion.div
        className="container"
        initial={{ opacity: 0, x: 100 }}
        animate={{ opacity: 1, x: 0 }}
        exit={{ opacity: 0, x: -100 }}
      >
        <div className="page">
          <button className="back-button" onClick={onBack}>
            <ArrowLeft size={20} /> Back to Home | होम पर वापस जाएं
          </button>

          <div className="header">
            <h1>📝 Quiz Mode | क्विज़ मोड</h1>
            <p className="subtitle">What topic do you want to practice? | आप किस विषय का अभ्यास करना चाहते हैं?</p>
            <p className="subtitle">Kis topic par quiz chahiye?</p>
          </div>

          <div className="topic-input-section">
            <input
              type="text"
              placeholder="Enter topic... | विषय दर्ज करें... (e.g., Photosynthesis, Fractions)"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              onKeyPress={(e) => e.key === 'Enter' && generateQuiz()}
              className="topic-input"
            />
            <motion.button
              className="generate-button"
              onClick={generateQuiz}
              disabled={isLoading}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              {isLoading ? <Loader className="spin" size={24} /> : <Send size={24} />}
              {isLoading ? 'Creating Quiz... | क्विज़ बना रहे हैं...' : 'Generate Quiz | क्विज़ बनाएं'}
            </motion.button>
          </div>

          <div className="example-topics">
            <p>💡 Example topics | उदाहरण विषय:</p>
            <div className="topic-chips">
              {['Photosynthesis', 'Fractions', 'India Geography', 'Simple Machines'].map((t) => (
                <button key={t} className="topic-chip" onClick={() => setTopic(t)}>
                  {t}
                </button>
              ))}
            </div>
          </div>
        </div>
      </motion.div>
    );
  }

  const question = quiz.questions[currentQuestion];

  return (
    <motion.div
      className="container"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <div className="page">
        <button className="back-button" onClick={resetQuiz}>
          <ArrowLeft size={20} /> New Topic | नया विषय
        </button>

        <div className="quiz-header">
          <h2>Topic | विषय: {quiz.topic}</h2>
          <div className="progress">
            Question | प्रश्न {currentQuestion + 1} / {quiz.questions.length}
          </div>
          <div className="score-badge">Score | स्कोर: {score}</div>
        </div>

        <AnimatePresence mode="wait">
          <motion.div
            key={currentQuestion}
            className="question-card"
            initial={{ opacity: 0, x: 50 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -50 }}
          >
            <h3>{question.question}</h3>

            <div className="options-grid">
              {question.options.map((option, index) => {
                let className = 'option';
                if (selectedAnswer !== null) {
                  if (index === question.correct) {
                    className += ' correct';
                  } else if (index === selectedAnswer) {
                    className += ' incorrect';
                  } else {
                    className += ' disabled';
                  }
                }

                return (
                  <motion.button
                    key={index}
                    className={className}
                    onClick={() => handleAnswer(index)}
                    disabled={selectedAnswer !== null}
                    whileHover={selectedAnswer === null ? { scale: 1.02 } : {}}
                    whileTap={selectedAnswer === null ? { scale: 0.98 } : {}}
                  >
                    <span className="option-letter">{String.fromCharCode(65 + index)}</span>
                    <span className="option-text">{option}</span>
                    {selectedAnswer !== null && index === question.correct && (
                      <CheckCircle size={24} />
                    )}
                    {selectedAnswer === index && index !== question.correct && (
                      <XCircle size={24} />
                    )}
                  </motion.button>
                );
              })}
            </div>

            {selectedAnswer !== null && (
              <motion.div
                className="explanation"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
              >
                <strong>Explanation:</strong> {question.explanation}
                
                <motion.button
                  className="next-question-button"
                  onClick={handleNextQuestion}
                  initial={{ opacity: 0, scale: 0.8 }}
                  animate={{ opacity: 1, scale: 1 }}
                  transition={{ delay: 0.3 }}
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  {currentQuestion < quiz.questions.length - 1 ? '➡️ Next Question | अगला प्रश्न' : '🏆 View Results | परिणाम देखें'}
                </motion.button>
              </motion.div>
            )}
          </motion.div>
        </AnimatePresence>
      </div>
    </motion.div>
  );
};

export default QuizMode;
