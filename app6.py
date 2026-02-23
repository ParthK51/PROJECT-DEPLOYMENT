import streamlit as st 

st.markdown("""

<style>
        .stButton > button
        {
          background-color:red;
          color:white;
          border-radius:20%;
        }
        .stTextInput >input
        {
          background-color:blue;
          color:green;
          border-radius:20%;
        }
      
""",unsafe_allow_html=True)







st.title("Registration Form")
name=st.text_input("Enter Your Name")
age=st.slider("select range",1,100)
gender=st.radio('select your gender',('male','female'))
address=st.text_input("enter your addresss")
city=st.selectbox("select your city",['Nashik','Mumbai','pune','Delhi'])

if st.button('Register'):
    st.write('Name',name)
    st.write('age',age)
    st.write('gender',gender)
    st.write('city',city)
    st.write('address',address)

