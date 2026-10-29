from pprint import pprint

from customer_dao import CustomerDAO
def main():
    dao = CustomerDAO("customers.db")

    all_customers =  dao.findAll()

    c1 = next(all_customers)
    print(c1)

    for customer in all_customers:
        print(customer)

if __name__=='__main__':
    main()
