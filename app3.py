import streamlit as st

st.title('BASIC CALCULATOR')

num1=st.number_input('enter first number',number_format['%d'])
num2=st.number_input('enter second number')

cals=st.selectbox('CHOOSE OPERATIONS',['ADD','SUB','MUL','DIV'])
if cals=='ADD':
        st.write('sum is=',num1+num2)
elif cals=='SUB':
        st.write('difference is=',num1-num2)
elif cals=='MUL':
        st.write('product is=',num1*num2)
elif cals=='DIV':
        if num2==0:
            st.write('division by zero is not allowed')
        else:
            st.write('quotient is=',num1/num2)
