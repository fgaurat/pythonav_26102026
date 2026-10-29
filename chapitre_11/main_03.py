from pprint import pprint
import streamlit as st
import time
import sqlite3
import pandas as pd

# uv run streamlit run main_01.py

DB_FILE = "customers.db"


@st.cache_data
def charger():
    print("charger() exécutée")
    time.sleep(2)  # base lente
    with sqlite3.connect(DB_FILE) as con:
        return pd.read_sql("SELECT * FROM customers_tbl", con)


def main():
    st.set_page_config(layout="wide")
    # charger_cache = st.cache_data(charger)
    start = time.perf_counter()
    df = charger()
    end = time.perf_counter()
    st.write(f"{len(df)} en {end-start:.2}s")
    st.slider("Le slider", 0, 100)


if __name__ == '__main__':
    main()
