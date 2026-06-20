import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import './LandingPage.css';

const LandingPage = ({ onEnter }) => {
  const [typedText, setTypedText] = useState('');
  const fullText = 'AI शिक्षण सहायक';

  // Typewriter effect for Hindi text
  useEffect(() => {
    let i = 0;
    const timer = setInterval(() => {
      if (i < fullText.length) {
        setTypedText(fullText.slice(0, i + 1));
        i++;
      } else {
        clearInterval(timer);
      }
    }, 100);
    return () => clearInterval(timer);
  }, []);

  const features = [
    { icon: '🧠', en: 'Explain Concepts', hi: 'अवधारणाएं समझें' },
    { icon: '📝', en: 'Smart Quizzes',    hi: 'स्मार्ट क्विज़' },
    { icon: '🎤', en: 'Voice Powered',    hi: 'आवाज़ से चलाएं' },
    { icon: '🌐', en: 'Hindi + English',  hi: 'हिंदी + अंग्रेज़ी' },
  ];

  return (
    <div className="landing-wrapper">

      {/* Animated floating blobs */}
      <div className="blob blob-1" />
      <div className="blob blob-2" />
      <div className="blob blob-3" />

      <div className="landing-content">

        {/* Badge */}
        <motion.div
          className="badge"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
        >
          🏫 Haryana Government Schools | हरियाणा सरकारी विद्यालय
        </motion.div>

        {/* Main Title */}
        <motion.div
          className="landing-title-block"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          <h1 className="landing-title-en">
            🎓 AI Teaching Assistant
          </h1>
          <h1 className="landing-title-hi">
            {typedText}<span className="cursor">|</span>
          </h1>
        </motion.div>

        {/* Subtitle */}
        <motion.p
          className="landing-subtitle"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.8 }}
        >
          Voice-Enabled Smart Classroom Co-Pilot<br />
          <span>आवाज़-सक्षम स्मार्ट कक्षा सहायक</span>
        </motion.p>

        {/* Feature pills */}
        <motion.div
          className="feature-pills"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
        >
          {features.map((f, i) => (
            <motion.div
              key={i}
              className="pill"
              initial={{ opacity: 0, scale: 0.8 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 1 + i * 0.15 }}
            >
              <span className="pill-icon">{f.icon}</span>
              <span className="pill-text">
                <span className="pill-en">{f.en}</span>
                <span className="pill-hi">{f.hi}</span>
              </span>
            </motion.div>
          ))}
        </motion.div>

        {/* CTA Button */}
        <motion.button
          className="cta-button"
          onClick={onEnter}
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 1.6, type: 'spring', stiffness: 200 }}
          whileHover={{ scale: 1.07 }}
          whileTap={{ scale: 0.95 }}
        >
          <span className="cta-en">Get Started</span>
          <span className="cta-divider">·</span>
          <span className="cta-hi">शुरू करें</span>
          <span className="cta-arrow">→</span>
        </motion.button>

        {/* Footer note */}
        <motion.p
          className="landing-footer"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 2 }}
        >
          Grades 6–10 · Hindi + English · Free to Use<br />
          कक्षा 6–10 · हिंदी + अंग्रेज़ी · मुफ़्त उपयोग
        </motion.p>

      </div>
    </div>
  );
};

export default LandingPage;
