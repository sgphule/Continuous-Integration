import streamlit as st

st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube, and fifth power.")

n = st.number_input("Enter an integer", value=1, step=1)

square = n ** 2
cube = n ** 3
fifth_power = n ** 5
def square_number(n):
    return n ** 2

def cube_number(n):
    return n ** 3

def fifth_power_of_number(n):
    return n ** 5

st.write(f"The square of {n} is: {square_number}")
st.write(f"The cube of {n} is: {cube_number}")
st.write(f"The fifth power of {n} is: {fifth_power_of_number}")

# execute using following command
# streamlit run src/power_calculator.py