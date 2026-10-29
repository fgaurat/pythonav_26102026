from pprint import pprint
import argparse
import csv
import sqlite3

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file_name')
    args = parser.parse_args()

    
    with sqlite3.connect("customers.db") as con:
        sql_insert = "INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address) VALUES (?,?,?,?,?)"
        with open(args.csv_file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                del row['id']
                con.execute(sql_insert,list(row.values()))






if __name__=='__main__':
    main()
