import streamlit as st
from knowledge_base import knowledge
from prompts import generate_response

#  Page Config 
st.set_page_config(
    page_title="EcoGuide AI",
    page_icon="🌱",
    layout="centered"
)

#  Ecosystem CSS 
st.markdown("""
<style>

/* ---- Background ---- */
body {
    background: linear-gradient(
        rgba(16, 185, 129, 0.15),
        rgba(5, 150, 105, 0.25)
    ),
    url("https://images.unsplash.com/photo-1441974231531-c6227db76b6e");
    background-size: cover;
    background-attachment: fixed;
}

/* ---- Main Glass Container ---- */
.main {
    background: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 18px;
    max-width: 720px;
    margin: auto;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    position: relative;
    z-index: 1;
}

/* ---- Header ---- */
.title {
    text-align: center;
    font-size: 2.4rem;
    font-weight: 700;
    color: #064e3b;
}
.subtitle {
    text-align: center;
    color: #065f46;
    margin-bottom: 2rem;
}

/* ---- Chat Styling ---- */
.stChatMessage {
    border-radius: 14px;
    padding: 10px;
}

/* ---- Floating Leaves ---- */
.leaf {
    position: fixed;
    top: -10%;
    font-size: 24px;
    opacity: 0.6;
    animation: float linear infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes float {
    0% {
        transform: translateY(0) translateX(0) rotate(0deg);
    }
    100% {
        transform: translateY(120vh) translateX(40px) rotate(360deg);
    }
}

</style>

<!-- Floating Leaves -->
<div class="leaf" style="left:8%; animation-duration:18s;">🍃</div>
<div class="leaf" style="left:22%; animation-duration:24s;">🍂</div>
<div class="leaf" style="left:40%; animation-duration:20s;">🍃</div>
<div class="leaf" style="left:58%; animation-duration:26s;">🍃</div>
<div class="leaf" style="left:72%; animation-duration:22s;">🍂</div>
<div class="leaf" style="left:88%; animation-duration:19s;">🍃</div>

""", unsafe_allow_html=True)

#  Header 
st.markdown('<div class="title">🌱 EcoGuide AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">An AI assistant inspired by Earth’s ecosystem</div>',
    unsafe_allow_html=True
)

# Chat History 
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

#  Chat Input 
user_input = st.chat_input("Ask about nature, climate, or sustainable living...")

if user_input:
    bot_response = generate_response(user_input, knowledge)
    st.session_state.chat_history.append(("user", user_input))
    st.session_state.chat_history.append(("assistant", bot_response))

# Display Chat 
for role, message in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(message)
