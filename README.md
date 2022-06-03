# Practica3

This is a project for the distributed systems class during my bachelor studies in Spain.
It is written in Python and should simulate a distributed system. The idea of the project is saving classes from the university server in a
google drive calendar. 

### Program

The flow of the program is linear. The user provides his credentials for the university server (using Bottle as a front end framework), then a web scrapper fetches the course data from the university server and sends it to another server. The server is implemented with the pika module from python. An additional script takes the course data from the server, and uploads them to google drive. Another script fetches the course from google drive and puts  them into the calendar. The scripts operate independently from each other.

### Technologies
  - bottle as front-end ramework
  - back-end consists of several independently operating python scripts
  - different google apis were used
