import streamlit as st

st.title('WELCOME TO CHATBOT')

st.write('Ask your question')

user_input=st.text_input('You:')

if st.button('ASK'):
    st.write('Hi your questions=',user_input)
    st.write('Processing your ans')
    