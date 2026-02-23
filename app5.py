import streamlit as st

st.markdown("""

<style>
        .stButton > button
        {
          background-color:red;
          color:white;
          border-radius:80%;
        }
      
        


""",unsafe_allow_html=True)













st.title(' welcome to basic streamlit app')

age=st.slider("select range",1,100)
city=st.selectbox("select your city",['Nashik','Mumbai','pune','Delhi'])

if st.button('show information'):
    st.write('age is',age)
    st.write('city is',city)