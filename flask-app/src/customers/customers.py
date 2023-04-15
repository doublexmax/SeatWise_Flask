from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from datetime import datetime


customers = Blueprint('customers', __name__)

# Get all customers from the DB
@customers.route('/customers', methods=['GET'])
def get_customers():
    cursor = db.get_db().cursor()

    cursor.execute("SELECT * FROM Customers")

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

# Get customer detail for customer with particular userID
@customers.route('/customers/<userID>', methods=['GET'])
def get_customer(userID):
    cursor = db.get_db().cursor()
    cursor.execute("SELECT * FROM Customers WHERE CustomerID = %s", (userID,))
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'


    return the_response

@customers.route('/customers', methods=['POST'])
def add_customers():
    cursor = db.get_db().cursor()

    cust_info = request.json



    query = "INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email, DOB, Street, City, State, ZipCode, Country)"

    return