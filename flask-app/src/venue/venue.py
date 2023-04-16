from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from datetime import datetime

venue = Blueprint('venue', __name__)

# Add a new venue  
@venue.route('/venues', methods=['POST'])
def add_venue():
    cursor = db.get_db().cursor()

    venue_info = request.json

    venue_tuple = f"('{venue_info.get('NewVenueName')}', '{venue_info.get('NewVenuePhone')}, '{venue_info.get('NewVenueEmail')}', \
                        '{venue_info.get('NewVenueStreet')}', '{venue_info.get('NewVenueCity')}', \
                        '{venue_info.get('NewVenueState')}', '{venue_info.get('NewVenueZipcode')}', '{venue_info.get('NewVenueCountry')}')"

    query = f"INSERT INTO Venues (VenueName, PhoneNumber, Email, Street, City, State, Zipcode, Country, OwnerID) VALUES {venue_tuple}"

    cursor.execute(query)

    db.get_db().commit()

    return "Successfully added new Venue"

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@venue.route('/venues/<VenueID>/tickets', methods=['GET'])
def get_tickets(VenueID):
    cursor = db.get_db().cursor()

    query = f"SELECT Type, Section, Seat_Row, Seat_Column, IFNULL(CustomerID, \"Available\") AS Customer FROM Tickets NATURAL JOIN Venues WHERE VenueID = %s"

    cursor.execute(query, (VenueID,))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@venue.route('/venues/<VenueID>/revenue', methods=['GET'])
def get_revenueo(VenueID):
    cursor = db.get_db().cursor()

    query = f"SELECT VenueName, Street, SUM(Price) AS Revenue FROM Tickets NATURAL JOIN Venues WHERE VenueID = %s AND CustomerID IS NOT NULL"

    cursor.execute(query, (VenueID,))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response