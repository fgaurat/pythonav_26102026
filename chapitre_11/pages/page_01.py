import streamlit as st


from customer_dao import CustomerDAO


@st.cache_data
def load_customers():
    dao = CustomerDAO("customers.db")
    return list(dao.findAll())


def main():
    st.write("# Customers")
    customers = load_customers()
    st.table(customers)


if __name__ == "__main__":
    main()
