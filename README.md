# Noter


A multi-service application that includes a Django authentication service and a Flask note taking service. Both services are containerized using Docker Compose and connected to a database with persistent volume.

### Prerequisites

- Docker
- Docker Compose


### Getting Started

- Clone the repository:
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
```
- Navigate to the project directory:
```bash
cd <your-repo-name>
```

- Start the application using Docker Compose:
```bash
docker-compose up
```
***Access the application at http://localhost:5050***

## Services

The application consists of the following services:

- Authentication Service:
The authentication service is built using Django and provides user authentication and registration. The service listens on port 8000.

- Note Taking Service:
The note taking service is built using Flask and provides CRUD functionality for notes. The service listens on port 5000.

- Database:
Both services are connected to a PostgreSQL database with a persistent volume.

## Configuration
The application can be configured using the following environment variables:

- POSTGRES_USER: The username for the PostgreSQL database (default: postgres).
- POSTGRES_PASSWORD: The password for the PostgreSQL database (default: password).
- POSTGRES_DB: The name of the PostgreSQL database (default: notes).
- AUTH_SERVICE_PORT: The port on which the authentication service listens (default: 8000).
- NOTE_SERVICE_PORT: The port on which the note taking service listens (default: 5000).

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

[MIT](https://choosealicense.com/licenses/mit/)

