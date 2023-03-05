# Dockersing-Three-Services
Implementing Dockers on a Django Authentication Service , a flask note taking service and Db Service

## Noter
This project includes three services: a Django authentication service, Flask note-taking service, and a database with persistent volume. All these services are containerized using Docker Compose.

Prerequisites
Docker
Docker Compose
Installation
Clone this repository:
sh
Copy code
git clone https://github.com/chethancheths/Dockersing-Three-Services.git
Build and start the containers:
sh
Copy code
cd <repository>
docker-compose up --build
Access the services:
Django authentication service: http://localhost:8000
Flask note-taking service: http://localhost:5000
