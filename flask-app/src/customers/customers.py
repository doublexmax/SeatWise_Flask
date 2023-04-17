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

# Get all customers names for the form from the DB
@customers.route('/customers/names', methods=['GET'])
def get_customers_form():
    cursor = db.get_db().cursor()

    cursor.execute("SELECT CONCAT(FirstName, ' ', LastName) as label, CustomerID as value FROM Customers")

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

# Get customer ticket detail for customer with particular userID
@customers.route('/customers/<userID>/tickets', methods=['GET'])
def get_customer_ticket(userID):
    cursor = db.get_db().cursor()

    query = "SELECT VenueName, Description, Date, Seat_Row, Seat_Column, Section FROM \
                Customers JOIN Tickets USING (CustomerID) JOIN Venues USING (VenueID) JOIN Performance USING (PerformanceID) WHERE CustomerID = %s"

    cursor.execute(query, (userID,))

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
def add_customer():
    cursor = db.get_db().cursor()

    cust_info = request.json

    cust_tuple = f"('{cust_info.get('CusFirstName', 'NULL')}', '{cust_info.get('CusLastName')}', '{cust_info.get('CusPhone')}', '{cust_info.get('CusEmail')}', '{cust_info.get('CusDOB')[:10]}', \
        '{cust_info.get('CusStreet')}', '{cust_info.get('CustCity')}', '{cust_info.get('CustState')}', '{cust_info.get('CustZipcode')}', '{cust_info.get('CustCountry')}')"
    
    query = f"INSERT INTO Customers (FirstName, LastName, PhoneNumber, Email, DOB, Street, City, State, ZipCode, Country) VALUES {cust_tuple}"

    cursor.execute(query)

    db.get_db().commit()

    return "Successfully added user into database."

@customers.route('/customers/<userID>/remove_dependent/<dependentID>', methods=['DELETE'])
def delete_dependent(userID, dependentID):
    cursor = db.get_db().cursor()
    
    query = f"UPDATE Dependent SET FirstName = 'unavailable', LastName = 'unavailable', \
        PhoneNumber = NULL, Email = NULL, Street = NULL, City = NULL, State  = NULL, \
            Zipcode  = NULL, Country  = NULL, Relationship = 'unavailable' WHERE Parent = %s and DependentID  = %s"
    
    cursor.execute(query, (userID, dependentID))

    db.get_db().commit()

    return "Deleted dependent"

@customers.route('/customers/<userID>', methods =['DELETE'])
def delete_account(userID):
    cursor = db.get_db().cursor()

    query = f"UPDATE Customers SET FirstName = 'unavailable', LastName = 'unavailable', \
        PhoneNumber = NULL, Email = NULL, Street = NULL, City = NULL, State  = NULL, \
            Zipcode = NULL, Country = NULL WHERE CustomerID = %s"
    
    cursor.execute(query, (userID,))

    db.get_db().commit()
    
    return "Deleted customer account"


@customers.route('/customers/<userID>/assign_ticket/<ticketID>', methods=['PUT'])
def assign_ticket(userID, ticketID):
    cursor = db.get_db().cursor()

    query = f"UPDATE Tickets SET CustomerID = %s WHERE TicketID = %s"
    
    cursor.execute(query, (userID, ticketID))

    db.get_db().commit()

    return the_response

# Getting Customers Last Name for Edit Form 
@customers.route('/customers/<cIDln>/lastname', methods=['GET'])
def get_customers_last_name(cIDln):
    
    return "Assigned ticket succesfully"
@customers.route('/customers/<userID>/dependents', methods = ['GET'])
def get_dependent(userID):
    cursor = db.get_db().cursor()

    query = f"SELECT CONCAT(FirstName, ' ', LastName) as label, DependentID as value From Dependent Where Parent = %s and FirstName !='unavailable'"

    cursor.execute(query, (userID,))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response
