# MySQL + Flask Boilerplate Project

This repo contains a boilerplate setup for spinning up 3 Docker containers: 
1. A MySQL 8 container for obvious reasons
2. A Python Flask container to implement a REST API
3. A Local AppSmith Server


## How to setup and start the containers
**Important** - you need Docker Desktop installed

1. Clone this repository.  
2. Create a file named `db_root_password.txt` in the `secrets/` folder and put inside of it the root password for MySQL. 
3. Create a file named `db_password.txt` in the `secrets/` folder and put inside of it the password you want to use for the a non-root user named webapp. 
4. In a terminal or command prompt, navigate to the folder with the `docker-compose.yml` file.  
5. Build the images with `docker compose build`
6. Start the containers with `docker compose up`.  To run in detached mode, run `docker compose up -d`. 

# Set up for DB 
   # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'abc123' # Change this the password you set
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'SeatWise'  # Change this to your DB name

Make sure you change `MYSQL_DATABASE_PASSWORD` to the password that you set in secrets under `db_root_password.txt`. 
Also, ensure that the database, mentioned here as `MYSQL_DATABASE_DB` to your own database name. 

Finally, the application registers all the imported routes with their corresponding URL prefixes by calling the app.`register_blueprint()` method.

In the provided code, four blueprints are registered with the application object:

1. **customers:** This blueprint handles routes related to customers, which are prefixed with `/c.`

2. **tickets**: This blueprint handles routes related to tickets, which are prefixed with `/t.`

3. **venue_owner**: This blueprint handles routes related to venue owners, which are prefixed with `/vo.`

4. **venue:** This blueprint handles routes related to venues, which are prefixed with `/v.`


You can now run the application on Appsmith by going to http://localhost:8080/ and deploying the latest version. 