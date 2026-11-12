import streamlit as st

# Page title and design setup
st.set_page_config(page_title="Special Question for You 💖", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    .main-title {
        font-size: 26px;
        font-weight: bold;
        text-align: center;
        color: #FF4B4B;
        margin-top: 30px;
        margin-bottom: 20px;
    }
    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'no_like_clicked' not in st.session_state:
    st.session_state.no_like_clicked = False
if 'wrong_choice' not in st.session_state:
    st.session_state.wrong_choice = False
if 'promise_taken' not in st.session_state:
    st.session_state.promise_taken = False

# ----------------- Step 1: Do you like Shiad? -----------------
if st.session_state.step == 1:
    st.markdown('<p class="main-title">Do you like Shiad? 🥺</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes ❤️"):
            st.session_state.step = 2
            st.session_state.no_like_clicked = False
            st.session_state.wrong_choice = False
            st.rerun()
            
    with col2:
        if st.button("No 💔"):
            st.session_state.no_like_clicked = True
            
    if st.session_state.no_like_clicked:
        st.error("⚠️ Please select the correct option! 😉")

# ----------------- Step 2: How do you consider me so perfect? -----------------
elif st.session_state.step == 2:
    st.markdown('<p class="main-title">How do you consider me so perfect? ✨</p>', unsafe_allow_html=True)
    
    if st.button("1. Brother 🧑‍🤝‍🧑"):
        st.session_state.wrong_choice = True
        
    if st.button("2. Stranger 🚶‍♂️"):
        st.session_state.wrong_choice = True
        
    if st.button("3. BF (Boyfriend) 🥰"):
        st.session_state.step = 3
        st.session_state.wrong_choice = False
        st.rerun()
        
    if st.session_state.wrong_choice:
        st.error("⚠️ Please select the correct option! (Think again! 😌)")

# ----------------- Step 3: Congratulations & Promise to Propose -----------------
elif st.session_state.step == 3:
    st.balloons()
    st.markdown('<p class="main-title" style="color: #28a745;">🎉 Congratulations! Best Choice Ever! ❤️</p>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown("<h4 style='text-align: center; color: #333;'>Now you have to make a little promise! 🤭</h4>", unsafe_allow_html=True)
    
    if not st.session_state.promise_taken:
        if st.button("Promise that you will propose to me nicely next time! 💍✨"):
            st.session_state.promise_taken = True
            st.rerun()
    else:
        st.success("✨ Promise Accepted! Looking forward to it! The story ends here... 😉❤️")
