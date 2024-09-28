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
1. Run Main.py:

When Main.py is run, it starts the process by authenticating with Google Drive and Google Calendar. You'll receive a link in the console that needs to be followed to authorize the app. This authentication allows the application to interact with your Google account services.

2. Provide University Server Credentials:

After authenticating Google services, you provide your credentials for the university server through a Bottle-based web interface. This triggers the web scraper to begin fetching course data from the university’s platform.

3. Run Add_to_Calendar.py:

Separately, run Add_to_Calendar.py that continuously monitors Google Drive for any new event data. Once the data is available, it reads the events and adds them to your Google Calendar.

## Program Flow
The project simulates a distributed system with the following components:

1. Web Scraper:

The web scraper (triggered after university credentials are provided) scrapes the course data from the university's online system. This data is sent as a message to the RabbitMQ server for further processing.

2. RabbitMQ Communication:

The scraped data is sent as a message to a RabbitMQ queue for further processing. 

3. Google Drive Integration:

Another process running independently listens for messages from RabbitMQ. Upon receiving a message, it formats the data and uploads it to Google Drive as a JSON file (test.json).

4. Google Calendar Integration:

Finally, another script continuously monitors Google Drive for the presence of test.json. When the file is found, its contents are downloaded and processed. The course schedule is then inserted as events into Google Calendar.

The entire system operates in a pipeline where component is decoupled:

Web Scraping → RabbitMQ → Google Drive → Google Calendar.

Potentially the web scrapping part does not work anymore due to changes on the website and it can't be verified since no valid credentials are known anymore.
