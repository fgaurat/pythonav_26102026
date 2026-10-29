from pprint import pprint
import streamlit as st
import time
import sqlite3
import pandas as pd
from customer_dao import CustomerDAO
# uv run streamlit run main_01.py

DB_FILE = "customers.db"


def charger():
    dao = CustomerDAO(DB_FILE)
    yield from dao.findAll()


@st.cache_data
def get_clients():
    return list(charger())


def main():
    st.set_page_config(layout="wide")
    # charger_cache = st.cache_data(charger)
    clients = get_clients()
    st.write(f"{len(clients)}")
    st.slider("Le slider", 0, 100)


if __name__ == '__main__':
    main()
