import streamlit as st


def main():

    pages = [
        st.Page("pages/page_01.py", title="La page 01",
                icon="😊", default=True),
        st.Page("pages/page_02.py", title="La page 02")
    ]

    st.navigation(pages).run()


if __name__ == "__main__":
    main()
