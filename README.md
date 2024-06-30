# Practica3

This is a project for the distributed systems class during my bachelor studies in Spain.
It is written in Python and should simulate a distributed system. The idea of the project is to save classes from the university server in a
Google Drive calendar. 

## Setup

To use RabbitMQ Chocolatey has to be installed. Do that by typing in Windows Powershell:

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Having Chocolatey installed one can install RabbitMQ by:

choco install rabbitmq

Then to start the RabbitMQ server: 

cd "C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.3\sbin"

.\rabbitmq-service.bat install

.\rabbitmq-service.bat start

Python 3.6 is used for the project. Dependencies are found in the requirements.txt of the project.

To run the project first run Main.py. In the console, a link will appear where you need to allow access to Google Drive and Google Calendar for the used account. Then start Add_to_Calendar.py separately.

### Program

The flow of the program is linear. The user provides his credentials for the university server (using Bottle as a front end framework), then a web scrapper fetches the course data from the university server and sends it to a rabbitMQ server. The server is implemented with the pika module from python. An additional script takes the course data from the server, and uploads them to google drive. Another script fetches the course from google drive and puts  them into the calendar. The scripts operate independently from each other.

### Technologies
  - bottle as front-end ramework
  - back-end consists of several independently operating python scripts
  - different google apis were used
