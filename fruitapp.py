import streamlit as st

st.set_page_config(page_title='Fruit App', page_icon=':tada:', layout='wide')

st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)


def main():
    st.title("Welcome to Apple and Banana Store")

    fruit = st.selectbox("Select a Fruit", ("Apples", "Bananas"))

    if fruit == "Apples":
        price = 1.0
    else:
        price = 0.5

    quantity = st.slider("Select Quantity", 1, 100)

    total_price = price * quantity

    st.write(f"Total price for {quantity} {fruit} is ${total_price:.2f}")

if __name__ == "__main__":
    main()
