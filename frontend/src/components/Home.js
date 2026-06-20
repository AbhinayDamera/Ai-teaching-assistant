import React from 'react';
import { motion } from 'framer-motion';
import { Brain, FileQuestion, HelpCircle } from 'lucide-react';

const Home = ({ onModeSelect }) => {
  const modes = [
    {
      id: 'explain',
      icon: <Brain size={80} />,
      title: 'Explain Concept | अवधारणा समझाएं',
      subtitle: 'Concept ko samjhao',
      description: 'Ask any question and get simple explanations | कोई भी सवाल पूछें और आसान जवाब पाएं',
      gradient: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
    },
    {
      id: 'quiz',
      icon: <FileQuestion size={80} />,
      title: 'Quiz Mode | क्विज़ मोड',
      subtitle: 'Quiz khelo',
      description: 'Practice with interactive quizzes | इंटरैक्टिव क्विज़ से अभ्यास करें',
      gradient: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'
    }
  ];

  return (
    <motion.div
      className="container"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      transition={{ duration: 0.5 }}
    >
      <div className="page">
        <div className="header">
          <motion.h1
            initial={{ scale: 0.5 }}
            animate={{ scale: 1 }}
            transition={{ type: 'spring', stiffness: 200 }}
          >
            🎓 AI Teaching Assistant | AI शिक्षण सहायक
          </motion.h1>
          <p className="subtitle">Voice-Enabled Classroom Co-Pilot | आवाज़-सक्षम कक्षा सहायक</p>
          <p className="subtitle">For Haryana Schools | हरियाणा स्कूलों के लिए</p>
        </div>

        <div className="mode-grid">
          {modes.map((mode, index) => (
            <motion.button
              key={mode.id}
              className="mode-card"
              style={{ background: mode.gradient }}
              onClick={() => onModeSelect(mode.id)}
              initial={{ opacity: 0, y: 50 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.2 }}
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              <div className="icon">{mode.icon}</div>
              <h2>{mode.title}</h2>
              <p style={{ fontSize: '1.2rem', fontWeight: 'bold', marginBottom: '10px' }}>
                {mode.subtitle}
              </p>
              <p>{mode.description}</p>
            </motion.button>
          ))}
        </div>

        <motion.div
          style={{ textAlign: 'center', marginTop: '60px', color: '#666' }}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          <HelpCircle size={24} style={{ display: 'inline-block', marginRight: '10px' }} />
          <p style={{ display: 'inline', fontSize: '1.1rem' }}>
            Click any mode to start | Apni pasand ka mode choose karo
          </p>
        </motion.div>
      </div>
    </motion.div>
  );
};

export default Home;
