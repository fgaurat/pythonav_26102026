from flask import Flask, render_template
from customer_dao import CustomerDAO
from typing import Generator, Any
from customer import Customer

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>index</p>"


@app.route("/hello/<name>")
def hello_world(name):

    # return f"<p>Hello {name}</p>"
    return render_template("hello.html", name=name)


@app.route("/customers")
def customers():
    dao = CustomerDAO("customers.db")
    all_customers: Generator[Customer, Any, None] = dao.findAll()
    return render_template("customers.html", customers=all_customers)
