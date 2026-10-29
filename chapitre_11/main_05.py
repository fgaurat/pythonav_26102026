from pprint import pprint
import streamlit as st
import time
import sqlite3
import pandas as pd
from customer_dao import CustomerDAO
# uv run streamlit run main_01.py

DB_FILE = "customers.db"


@st.cache_resource
def connexion_bug():
    return sqlite3.connect(DB_FILE)


@st.cache_resource
def connexion_ok():
    # chaque rerun tourne dans un nouveau thread : il faut l'autoriser.
    # Pour des écritures concurrentes, ajouter un threading.Lock (voir dao.py)
    return sqlite3.connect(DB_FILE, check_same_thread=False)


def main():
    st.set_page_config(layout="wide")

    # charger_cache = st.cache_data(charger)
    con = connexion_bug()
    # con = connexion_ok()
    n = con.execute("SELECT COUNT(*) FROM customers_tbl").fetchone()[0]
    st.write(f"{n} clients")
    st.button("Relancer le script")


if __name__ == '__main__':
    main()
