from pprint import pprint
import streamlit as st

# uv run streamlit run main_01.py


def main():
    st.set_page_config(layout="wide")
    st.write("""
    Hello, *World!* :sunglasses:
    # Titre 3
    """)

    title = st.text_input("Movie title", "Life of Brian")

    if st.button("Click !"):
        st.write("The current movie title is", title)


if __name__ == '__main__':
    main()
