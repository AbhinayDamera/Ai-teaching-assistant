import React, { useState } from 'react';
import { AnimatePresence } from 'framer-motion';
import LandingPage from './components/LandingPage';
import Home from './components/Home';
import ExplainMode from './components/ExplainMode';
import QuizMode from './components/QuizMode';
import './App.css';

function App() {
  const [currentMode, setCurrentMode] = useState('landing'); // landing, home, explain, quiz

  return (
    <div className="App">
      <AnimatePresence mode="wait">
        {currentMode === 'landing' && (
          <LandingPage key="landing" onEnter={() => setCurrentMode('home')} />
        )}
        {currentMode === 'home' && (
          <Home key="home" onModeSelect={setCurrentMode} />
        )}
        {currentMode === 'explain' && (
          <ExplainMode key="explain" onBack={() => setCurrentMode('home')} />
        )}
        {currentMode === 'quiz' && (
          <QuizMode key="quiz" onBack={() => setCurrentMode('home')} />
        )}
      </AnimatePresence>
    </div>
  );
}

export default App;
