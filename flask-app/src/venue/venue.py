from flask import Blueprint, request, jsonify, make_response
import json
from src import db
from datetime import datetime

venue = Blueprint('venue', __name__)

# This is a base route
# we simply return a string.  
@venue.route('/venues')
def get_venues():
    return ('<h1>Hello from your web app!!</h1>')

# This is a sample route for the /test URI.  
# as above, it just returns a simple string. 
@venue.route('/test')
def tester():
    return "<h1>this is a test!</h1>"