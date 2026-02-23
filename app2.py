import streamlit as st

st.title(' welcome to basic streamlit app')

age=st.slider("select range",1,100)
city=st.selectbox("select your city",['Nashik','Mumbai','pune','Delhi'])

if st.button('show information'):
    st.write('age is',age)
    st.write('city is',city)