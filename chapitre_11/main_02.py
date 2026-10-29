from pprint import pprint
import streamlit as st

# uv run streamlit run main_01.py


def main():
    st.set_page_config(layout="wide")

    st.session_state.setdefault("cpt", 0)

    if st.button('inc'):
        st.session_state.cpt += 1
        st.metric("Le cpt", st.session_state.cpt)


if __name__ == '__main__':
    main()
