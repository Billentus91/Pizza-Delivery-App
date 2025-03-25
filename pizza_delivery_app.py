
import streamlit as st

def calculate_bill(size, pepperoni, cheese):
    total = 0

    if size == "S":
        total = 15
    elif size == "M":
        total = 20
    elif size == "L":
        total = 25
    else:
        return "Invalid Size"

    if pepperoni == "Y":
        total += 2 if size == "S" else 3

    if cheese == "Y":
        total += 1

    return f"Your total bill is ${total}"

st.title("🍕 Python Pizza Order")

# User inputs
size = st.radio("What size of pizza do you want?", ["S", "M", "L"])
pepperoni = st.radio("Do you want pepperoni?", ["Y", "N"])
cheese = st.radio("Do you want extra cheese?", ["Y", "N"])

if st.button("Calculate Bill"):
    total = calculate_bill(size, pepperoni, cheese)
    st.success(total)
