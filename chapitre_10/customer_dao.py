
import sqlite3

from customer import Customer


class CustomerDAO:

    def __init__(self, db_file) -> None:
        self._con = sqlite3.connect(db_file)

    def delete(self, id):
        cur = self._con.cursor()
        sql = "DELETE FROM customers_tbl WHERE id=?"
        cur.execute(sql, id)
        self._con.commit()

        return cur.rowcount > 0

    def findAll(self):
        cur = self._con.cursor()

        res = cur.execute("SELECT * FROM customers_tbl")

        # for id,first_name,last_name,email,gender,ip_address in res.fetchall():
        #     c = Customer(id,first_name,last_name,email,gender,ip_address)

        # customers = []
        # for row in res.fetchall():
        #     c = Customer(*row)
        #     customers.append(c)

        # # customers = [Customer(*row) for row in res.fetchall()]
        # return customers

        for row in res.fetchall():
            yield Customer(*row)

    def __del__(self):
        self._con.close()
