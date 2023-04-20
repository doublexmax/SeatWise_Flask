# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
2. A Python Flask container to implement a REST API
3. A Local AppSmith Server


## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a \\ non-root user named webapp. 
4. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 
<br> <br>

# Set up for DB 
   ## These are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root' 
    app.config['MYSQL_DATABASE_PASSWORD'] = 'abc123' # Change this the password you set 
    app.config['MYSQL_DATABASE_HOST'] = 'db' 
    app.config['MYSQL_DATABASE_PORT'] = 3306 
    app.config['MYSQL_DATABASE_DB'] = 'SeatWise'  # Change this to your DB name 

Make sure you change `MYSQL_DATABASE_PASSWORD` to the password that you set in secrets under `db_root_password.txt`. 
Also, ensure that the database, mentioned here as `MYSQL_DATABASE_DB` to your own database name. <br>

Finally, the application registers all the imported routes with their corresponding URL prefixes by calling the app.`register_blueprint()` method.
<br> <br>

# Code Explanation
## In the provided code, four blueprints are registered with the application object: <br>

1. **customers:** This blueprint handles routes related to customers, which are prefixed with `/c.`
    
    Here are some of the actions that can be performed:
    1. `GET /customers:` Retrieve a list of all customers in the database.
    2. `GET /customers/names:` Retrieve a list of customer names and IDs that can be used for a form.
    3. `GET /customers/<userID>:` Retrieve details about a specific customer identified by their ID.
    4. `GET /customers/<userID>/tickets:` Retrieve a list of tickets purchased by a specific customer identified by their ID.
    5. `GET /customers/<userID>/dependents:` Retrieve a list of dependents associated with a specific customer identified by their ID.
    6. `GET /customers/<cIDInf>/info:` Retrieve customer information for a specific customer identified by their ID for an edit form.
    7. `GET /customers/fanof: `Retrieve a list of artists that a customer can select as their favorite.
    8. `GET /customers/dependent/<cIdDInf>/info:` Retrieve dependent information for a specific dependent identified by their ID for an edit form
    9. `PUT /customer/<customer_id>:` Updating a customer 
    10. `POST /customer`: creating a new customer 
    11. `DELETE /customer/<customer_id>:` Deleteing customer 
<br> <br>

2. **tickets**: This blueprint handles routes related to tickets, which are prefixed with `/t.`
    
    Here are some of the actions that can be performed:
    1. `GET /tickets/:` Returns a list of all the tickets in the database.
    2. `GET /tickets/<ticketID>`: Returns the ticket with the specified ticketID.
<br> <br>

3. **venue_owner**: This blueprint handles routes related to venue owners, which are prefixed with `/vo.`
   
    Here are some of the actions that can be performed:
    1. `GET /venues:` Retrieve a list of all venues in the database.
    2. `GET /venues/names:` Retrieve a list of venue names and IDs that can be used for a form.
    3. `GET /venues/<venueID>:` Retrieve details about a specific venue identified by its ID.
    4. `GET /venues/<venueID>/events:` Retrieve a list of events hosted by a specific venue identified by its ID.
    5. `GET /venues/<venueID>/available_dates:` Retrieve a list of available dates for a specific venue identified by its ID.
    6. `GET /venues/<vIDInf>/info:` Retrieve venue information for a specific venue identified by its ID for an edit form.
    7. `PUT /venues/<venueID>`: Updating a venue.
    8. `POST /venues:` creating a new venue.
    9. `DELETE /venues/<venueID>:` Deleting a venue.
<br> <br>

4. **venue:** This blueprint handles routes related to venues, which are prefixed with `/v.`

    Here are some of the actions that can be performed:
    1. `GET /venues:` Retrieve a list of all venues in the database.
    2. `GET /venues/names:` Retrieve a list of venue names and IDs that can be used for a form.
    3. `GET /venues/<venueID>:` Retrieve details about a specific venue identified by its ID.
    4. `GET /venues/<venueID>/events:` Retrieve a list of events hosted by a specific venue identified by its ID.
    5. `GET /venues/<venueID>/available_dates:` Retrieve a list of available dates for a specific venue identified by its ID.
    6. `GET /venues/<vIDInf>/info:` Retrieve venue information for a specific venue identified by its ID for an edit form.
    7. `PUT /venues/<venueID>:` Updating a venue.
    8. `POST /venues:` creating a new venue.
    9. `DELETE /venues/<venueID>:` Deleting a venue.

You can now run the application on Appsmith by going to http://localhost:8080/ and deploying the latest version. 

<ul> Link To Video Demonstration: </ul> <a href="https://northeastern.zoom.us/rec/play/5Kv9nlv8rypzBqHVRW2vYOSnwuXV6L1FyU2YFOzm-XSTaxEAZWEioQBdiFRfDXLaE6wMPl14WO4GZCNZ.klZxLDk9DZ-XOO0v?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fnortheastern.zoom.us%2Frec%2Fshare%2F7zzjROW4j1u3ocCzYFgG9uqQy1pHCBOvM-YV-rINzorqxitRIs3dzXq1TmWSv_d7.3cwp1Gu_j-Jx6uML" />
