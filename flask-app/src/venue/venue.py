from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from datetime import datetime

venue = Blueprint('venue', __name__)

# Add a new venue  
@venue.route('/venues/<OwnerID>', methods=['POST'])
def add_venue(OwnerID):
    cursor = db.get_db().cursor()

    venue_info = request.json

    venue_tuple = f"('{venue_info.get('NewVenueName')}', '{venue_info.get('NewVenuePhone')}', '{venue_info.get('NewVenueEmail')}', \
                        '{venue_info.get('NewVenueStreet')}', '{venue_info.get('NewVenueCity')}', \
                        '{venue_info.get('NewVenueState')}', '{venue_info.get('NewVenueZipcode')}', '{venue_info.get('NewVenueCountry')}', \
                        '{venue_info.get('Venue_Owner')}')"

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

# This is to delete the venue by a venue owner
@venue.route('/venues/<VenueID>', methods=['DELETE'])
def delete_venue(VenueID):
    cursor = db.get_db().cursor()

    query = f"UPDATE Venues SET PhoneNumber = 'Unavailable', Email = 'Unavailable', Street = 'Unavailable', City = 'Unavailable', \
        State = 'Unavailable', Zipcode = 'Unavailable', Country = 'Unavailable' WHERE VenueID = %s"

    cursor.execute(query, (VenueID,))

    db.get_db().commit()

    return "Deleted"

# This is to delete the venue by a venue owner
@venue.route('/venues/<VenueID>/performances', methods=['GET'])
def venue_performances(VenueID):
    cursor = db.get_db().cursor()

    query = f"SELECT Description as label, PerformanceID as value FROM Venues JOIN Performance USING(VenueID) WHERE VenueID = %s"

    cursor.execute(query, (VenueID,))

    db.get_db().commit()

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

# Return all venue's a venue owner owns
@venue.route('/venues/form', methods=['GET'])
def get_venues():
    cursor = db.get_db().cursor()

    query = "SELECT VenueName as label, VenueID as value FROM Venues"

    cursor.execute(query)

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

@venue.route('/tickets/<performanceID>/form', methods=['GET'])
def get_ticket(performanceID):
    cursor = db.get_db().cursor()

    query = "SELECT CONCAT(Section, Seat_Row, Seat_Column, ' Price: $', Price) as label, TicketID AS value FROM Tickets WHERE PerformanceID = %s AND CustomerID IS NULL"

    cursor.execute(query, (performanceID))
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