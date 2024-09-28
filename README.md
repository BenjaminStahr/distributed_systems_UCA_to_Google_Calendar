# Distributed Systems Class Project

This is a Python-based project developed for a distributed systems class during my bachelor's studies in Spain. The application simulates a distributed system where university classes are scraped from a server and saved into a Google Drive calendar.

## Setup

1. Install RabbitMQ with Chocolatey:
To run this project, RabbitMQ is required. Install it using Chocolatey in Windows PowerShell:

Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

Once Chocolatey is installed, install RabbitMQ:

choco install rabbitmq

To start the RabbitMQ server:

cd "C:\Program Files\RabbitMQ Server\rabbitmq_server-3.13.3\sbin"

.\rabbitmq-service.bat install

.\rabbitmq-service.bat start

2. Set up Python:

The project uses Python 3.6. Install any dependencies by running:

pip install -r requirements.txt

Python 3.6 is used for the project. Dependencies are found in the requirements.txt of the project.

## Execution
Run Main.py:

When Main.py is run, it starts the process by authenticating with Google Drive and Google Calendar. You'll receive a link in the console that needs to be followed to authorize the app. This authentication allows the application to interact with your Google account services.

To run the project first run Main.py. In the console, a link will appear where you need to allow access to Google Drive and Google Calendar for the used account. Then start Add_to_Calendar.py separately.

### Program

The flow of the program is linear. The user provides his credentials for the university server (using Bottle as a front end framework), then a web scrapper fetches the course data from the university server and sends it to a rabbitMQ server. The server is implemented with the pika module from Python. An additional script takes the course data from the server and uploads them to google drive. Another script fetches the course from Google Drive and puts  it into the calendar. The scripts operate independently from each other. 

Potentially the web scrapping part does not work anymore due to changes on the website and it can't be verified since no valid credentials are known anymore.

### Technologies
  - bottle as front-end ramework
  - back-end consists of several independently operating python scripts
  - different google apis were used
