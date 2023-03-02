import streamlit as st

def main():
    st.title("Welcome to Apple and Banana Store")

    fruit = st.selectbox("Select a Fruit", ("Apples", "Bananas"))

    if fruit == "Apples":
        price = 1.0
    else:
        price = 0.5

    quantity = st.slider("Select Quantity", 1, 10)

    total_price = price * quantity

    st.write(f"Total price for {quantity} {fruit} is ${total_price:.2f}")

if __name__ == "__main__":
    main()
