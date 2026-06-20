import streamlit as st
import os
from dotenv import load_dotenv
from utils.voice_handler import VoiceHandler
from utils.ai_teacher import AITeacher
from utils.quiz_generator import QuizGenerator
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Teaching Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for smart board optimization
st.markdown("""
<style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        width: 100%;
        height: 80px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 10px 0;
    }
    .concept-box {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 20px 0;
        font-size: 20px;
        line-height: 1.8;
    }
    .quiz-box {
        background-color: #fff3cd;
        padding: 25px;
        border-radius: 15px;
        border: 3px solid #ffc107;
        margin: 20px 0;
        font-size: 22px;
    }
    .title-text {
        font-size: 48px;
        text-align: center;
        color: #1e3a8a;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .status-text {
        font-size: 24px;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .listening {
        background-color: #dcfce7;
        color: #166534;
    }
    .processing {
        background-color: #fef3c7;
        color: #92400e;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'voice_handler' not in st.session_state:
    st.session_state.voice_handler = VoiceHandler()
if 'ai_teacher' not in st.session_state:
    st.session_state.ai_teacher = AITeacher()
if 'quiz_generator' not in st.session_state:
    st.session_state.quiz_generator = QuizGenerator()
if 'current_mode' not in st.session_state:
    st.session_state.current_mode = 'home'
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'current_quiz' not in st.session_state:
    st.session_state.current_quiz = None
if 'quiz_index' not in st.session_state:
    st.session_state.quiz_index = 0
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0

# Header
st.markdown('<div class="title-text">🎓 AI Teaching Assistant 🎤</div>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 20px; color: #64748b;">Voice-Enabled Classroom Co-Pilot for Haryana Schools</p>', unsafe_allow_html=True)

# Main interface
if st.session_state.current_mode == 'home':
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Choose a Mode:")
        
        if st.button("🧠 Explain Concept\n(Concept ko samjhao)", key="explain_btn"):
            st.session_state.current_mode = 'explain'
            st.rerun()
        
        if st.button("📝 Quiz Mode\n(Quiz khelo)", key="quiz_btn"):
            st.session_state.current_mode = 'quiz'
            st.rerun()
        
        if st.button("ℹ️ Help\n(Madad)", key="help_btn"):
            st.session_state.current_mode = 'help'
            st.rerun()

elif st.session_state.current_mode == 'explain':
    st.markdown("### 🧠 Live Concept Simplification")
    st.markdown("**Press the button and speak in Hindi, English, or Hinglish**")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("🎤 Speak Your Question\n(Apna sawal bolo)", key="speak_btn"):
            status_placeholder = st.empty()
            status_placeholder.markdown('<div class="status-text listening">🎤 Listening... Bol rahe hain...</div>', unsafe_allow_html=True)
            
            # Get voice input
            question = st.session_state.voice_handler.listen()
            
            if question:
                status_placeholder.markdown(f'<div class="status-text">📝 You asked: **{question}**</div>', unsafe_allow_html=True)
                
                # Process with AI
                with st.spinner("🤔 Thinking... Soch raha hoon..."):
                    response = st.session_state.ai_teacher.explain_concept(question)
                
                # Display response
                st.markdown(f'<div class="concept-box">{response["explanation"]}</div>', unsafe_allow_html=True)
                
                # Show image if available
                if response.get("image_url"):
                    st.image(response["image_url"], use_column_width=True)
                
                # Speak the response
                st.session_state.voice_handler.speak(response["explanation"])
                
                # Add to history
                st.session_state.conversation_history.append({
                    "question": question,
                    "answer": response["explanation"]
                })
            else:
                status_placeholder.markdown('<div class="status-text" style="background-color: #fee2e2; color: #991b1b;">❌ Could not understand. Kripya phir se bolo.</div>', unsafe_allow_html=True)
    
    with col2:
        if st.button("🏠 Home", key="home_btn"):
            st.session_state.current_mode = 'home'
            st.rerun()
    
    # Show conversation history
    if st.session_state.conversation_history:
        st.markdown("---")
        st.markdown("### 📜 Recent Explanations")
        for i, item in enumerate(reversed(st.session_state.conversation_history[-3:])):
            with st.expander(f"Q: {item['question'][:50]}..."):
                st.write(item['answer'])

elif st.session_state.current_mode == 'quiz':
    st.markdown("### 📝 Voice-Triggered Quiz Mode")
    
    if st.session_state.current_quiz is None:
        st.markdown("**What topic do you want to practice? (Kis topic par quiz chahiye?)**")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            if st.button("🎤 Speak Topic Name\n(Topic ka naam bolo)", key="quiz_topic_btn"):
                status_placeholder = st.empty()
                status_placeholder.markdown('<div class="status-text listening">🎤 Listening for topic...</div>', unsafe_allow_html=True)
                
                topic = st.session_state.voice_handler.listen()
                
                if topic:
                    status_placeholder.markdown(f'<div class="status-text">📚 Generating quiz on: **{topic}**</div>', unsafe_allow_html=True)
                    
                    with st.spinner("📝 Creating quiz... Quiz bana rahe hain..."):
                        quiz_data = st.session_state.quiz_generator.generate_quiz(topic)
                        st.session_state.current_quiz = quiz_data
                        st.session_state.quiz_index = 0
                        st.session_state.quiz_score = 0
                    
                    # Announce quiz start
                    intro = f"Theek hai! {topic} ke upar {len(quiz_data['questions'])} questions hain. Chalo shuru karte hain!"
                    st.session_state.voice_handler.speak(intro)
                    time.sleep(1)
                    st.rerun()
        
        with col2:
            if st.button("🏠 Home", key="home_quiz_btn"):
                st.session_state.current_mode = 'home'
                st.rerun()
    
    else:
        # Display current question
        if st.session_state.quiz_index < len(st.session_state.current_quiz['questions']):
            question = st.session_state.current_quiz['questions'][st.session_state.quiz_index]
            
            st.markdown(f"### Question {st.session_state.quiz_index + 1}/{len(st.session_state.current_quiz['questions'])}")
            st.markdown(f'<div class="quiz-box"><strong>Q: {question["question"]}</strong></div>', unsafe_allow_html=True)
            
            # Display options
            for i, option in enumerate(question['options']):
                st.markdown(f"**{chr(65+i)}.** {option}", unsafe_allow_html=False)
            
            col1, col2, col3 = st.columns([2, 2, 1])
            
            with col1:
                if st.button("🎤 Speak Answer (A, B, C, or D)\n(Jawab bolo)", key="answer_btn"):
                    # Announce question
                    st.session_state.voice_handler.speak(f"Question number {st.session_state.quiz_index + 1}. {question['question']}")
                    time.sleep(0.5)
                    
                    status_placeholder = st.empty()
                    status_placeholder.markdown('<div class="status-text listening">🎤 Listening for answer...</div>', unsafe_allow_html=True)
                    
                    answer = st.session_state.voice_handler.listen()
                    
                    if answer:
                        # Parse answer (A, B, C, D or full text)
                        answer = answer.strip().upper()
                        if len(answer) > 0:
                            answer_letter = answer[0] if answer[0] in ['A', 'B', 'C', 'D'] else None
                            
                            if answer_letter:
                                answer_index = ord(answer_letter) - 65
                                correct_index = question['correct']
                                
                                if answer_index == correct_index:
                                    st.session_state.quiz_score += 1
                                    feedback = f"Bahut badhiya! Sahi jawab hai. {question.get('explanation', '')}"
                                    st.success(f"✅ Correct! {question.get('explanation', '')}")
                                else:
                                    correct_letter = chr(65 + correct_index)
                                    feedback = f"Galat jawab. Sahi jawab hai {correct_letter}. {question.get('explanation', '')}"
                                    st.error(f"❌ Wrong! Correct answer is {correct_letter}. {question.get('explanation', '')}")
                                
                                st.session_state.voice_handler.speak(feedback)
                                time.sleep(2)
                                
                                st.session_state.quiz_index += 1
                                time.sleep(2)
                                st.rerun()
            
            with col2:
                if st.button("⏭️ Skip Question\n(Chhodo)", key="skip_btn"):
                    st.session_state.quiz_index += 1
                    st.rerun()
            
            with col3:
                if st.button("🏠 Home", key="home_quiz_active_btn"):
                    st.session_state.current_quiz = None
                    st.session_state.current_mode = 'home'
                    st.rerun()
        
        else:
            # Quiz completed
            score_percent = (st.session_state.quiz_score / len(st.session_state.current_quiz['questions'])) * 100
            st.markdown(f'<div class="quiz-box">', unsafe_allow_html=True)
            st.markdown(f"### 🎉 Quiz Complete!")
            st.markdown(f"### Score: {st.session_state.quiz_score}/{len(st.session_state.current_quiz['questions'])}")
            st.markdown(f"### Percentage: {score_percent:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)
            
            feedback = f"Quiz khatam! Aapka score hai {st.session_state.quiz_score} out of {len(st.session_state.current_quiz['questions'])}. "
            if score_percent >= 80:
                feedback += "Bahut badhiya performance!"
            elif score_percent >= 60:
                feedback += "Accha hai, thoda aur practice karo!"
            else:
                feedback += "Koi baat nahi, phir se try karo!"
            
            st.session_state.voice_handler.speak(feedback)
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("🔄 New Quiz\n(Naya quiz)", key="new_quiz_btn"):
                    st.session_state.current_quiz = None
                    st.session_state.quiz_index = 0
                    st.session_state.quiz_score = 0
                    st.rerun()
            
            with col2:
                if st.button("🏠 Home", key="home_quiz_complete_btn"):
                    st.session_state.current_quiz = None
                    st.session_state.current_mode = 'home'
                    st.rerun()

elif st.session_state.current_mode == 'help':
    st.markdown("### ℹ️ How to Use / Kaise Use Karein")
    
    st.markdown("""
    <div class="concept-box">
    <h3>🧠 Explain Concept Mode</h3>
    <ul>
        <li>Press the microphone button</li>
        <li>Ask your question in Hindi, English, or Hinglish</li>
        <li>Get explanation with visuals</li>
        <li><strong>Example:</strong> "Photosynthesis ko explain karo"</li>
    </ul>
    
    <h3>📝 Quiz Mode</h3>
    <ul>
        <li>Press microphone and say the topic</li>
        <li>Listen to questions</li>
        <li>Speak your answer (A, B, C, or D)</li>
        <li>Get instant feedback</li>
    </ul>
    
    <h3>💡 Tips</h3>
    <ul>
        <li>Speak clearly near the microphone</li>
        <li>You can mix Hindi and English</li>
        <li>Use simple words for best results</li>
        <li>Works best in quiet environment</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🏠 Back to Home", key="home_help_btn"):
        st.session_state.current_mode = 'home'
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 20px;">
    <p>🎓 Built for Haryana Government Schools | Voice-First Education</p>
    <p style="font-size: 14px;">Optimized for Smart Board Display</p>
</div>
""", unsafe_allow_html=True)
