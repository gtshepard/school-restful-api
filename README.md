## Schoolify 
- Full Stack Application Developed by Garrison Shepard
	- ReactJS + Flask + psycopg2 + PostgreSQL
- Still in active development 


### Schoolify Front End 
- ReactJs project
- makes request to Schoolify RESTful Api via fetch 


### Schoolify Restful Api 
 - a school database with a Restful API interface written in python using 
   - Flask as a web framework 
   - pyscopg2 for connection to the database
   - postgreSQL as a Database Management System 


### How Fire Up This App
 - Start the Server for Web Service 
   - pipevn lock
   - export FLASK_APP=app.py 
   - flask run 
	
 - Start the for server for the front-end
 	- navigiate to front-end/schoolify/ and run ```npm start```
	
### A Note on Database Configuration 
 - must install postgreSQL and set up a role in the database 
 - in app.py file set your username and password for connection to the database
