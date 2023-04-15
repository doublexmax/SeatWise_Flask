from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from datetime import datetime

# Create a new Flask Blueprint
# IMPORTANT: Notice in the routes below, we are adding routes to the 
# blueprint object, not the app object.
venue_owner = Blueprint('venue_owners', __name__)

# Return all venue's a venue owner owns
@venue_owner.route('/venues/<VenueOwnerID>')
def get_owner_venues(VenueOwnerID):
    cursor = db.get_db().cursor()

    query = "SELECT * FROM Venues WHERE OwnerID = %s"

    cursor.execute(query, (VenueOwnerID,))

    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'

    return the_response

# Get Venue Owner
@venue_owner.route('/venue_owner')
def tester():
    return "<h1>this is a test!</h1>"