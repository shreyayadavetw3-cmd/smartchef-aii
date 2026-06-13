import streamlit as st

st.title("🍳 SmartChef AI")

budget = st.number_input("Daily Budget (₹)", value=200)

ingredients = st.text_area("Available Ingredients")

if st.button("Generate Meal Plan"):

    st.subheader("🥞 Breakfast")
    st.write("Vegetable Poha")

    st.subheader("🍛 Lunch")
    st.write("Dal Rice")

    st.subheader("🍲 Dinner")
    st.write("Paneer Bhurji with Roti")

    st.subheader("🛒 Grocery List")
    st.write("""
    - Onion
    - Tomato
    - Dal
    - Rice
    - Paneer
    """)

    st.subheader("💰 Budget Analysis")
    st.success("Estimated Cost ₹180 - Within Budget")

    st.subheader("🔄 Substitutions")
    st.write("""
    Paneer → Tofu
    Rice → Millet
    """)
