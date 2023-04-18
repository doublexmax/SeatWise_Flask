from flask import Blueprint, request, jsonify, make_response
import json
from src import db


tickets = Blueprint('tickets', __name__)

# Get all the tickets from the database
@tickets.route('/tickets', methods=['GET'])
def get_products():
    # get a cursor object from the database
    cursor = db.get_db().cursor()

    # use cursor to query the database for a list of tickets
    cursor.execute('SELECT * FROM Tickets')

    # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)

# Get the specific ticket info given the ticketID
@tickets.route('/tickets/<ticketID>', methods=['GET'])
def get_ticket(ticketID):
    cursor = db.get_db().cursor()

    query = "SELECT * FROM Tickets WHERE TicketID = %s"

    cursor.execute(query, (ticketID))
       # grab the column headers from the returned data
    column_headers = [x[0] for x in cursor.description]

    # create an empty dictionary object to use in 
    # putting column headers together with data
    json_data = []

    # fetch all the data from the cursor
    theData = cursor.fetchall()

    # for each of the rows, zip the data elements together with
    # the column headers. 
    for row in theData:
        json_data.append(dict(zip(column_headers, row)))

    return jsonify(json_data)