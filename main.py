import streamlit as st


def display(query):
    pass


def connection():
    pass


if __name__ == '__main__':
    connection()
    st.title('Enter query')
    q = st.text_input('', placeholder='Select * from ______')
    st.button('RUN', on_click=display(q))
