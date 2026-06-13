import streamlit as st

st.title("🍳 SmartChef AI")

budget = st.number_input("Daily Budget (₹)", value=200)

ingredients = st.text_area("Available Ingredients")

if st.button("Generate Plan"):
    st.success("Meal plan generated!")