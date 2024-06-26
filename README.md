# FinalProject_DE_DigitalSkola

![Untitled-2024-06-23-1930](https://github.com/andrewsuadnya/FinalProject_DE_DigitalSkola/assets/90898706/0dfb04d3-f428-4dfe-bf5b-6bf8bf9cdc8d)

1. Sign Up Finnhub https://finnhub.io/docs/api/symbol-search
2. Sign Up/Login to MongoDB Atlas and create cluster or use existing cluster:
https://cloud.mongodb.com
3. Copy and paste this Airflow Docker compose to docker-compose.yaml:
https://shrib.com/#Phillip3yM6o5k
4. Create new database in Postgres Airflow to load output table
5. Create Python code to load news from finnhub to MongoDB Atlas
6. Create Python code to analyze news from MongoDB and load it to Postgres
7. Schedule the point 5 and 6 using Airflow DAG

-------------------------------------------------------------------------------

## Introduction
This project is a Data Engineering Final Project for Digital Skola. It includes various components such as data extraction, transformation, loading, and analysis using tools like Docker, PostgreSQL, MongoDB, and sentiment analysis libraries.

## Features
- Data extraction from APIs
- Data loading into MongoDB and PostgreSQL
- Sentiment analysis on extracted data
- Dockerized environment for easy setup and deployment
- Scheduler for automated tasks using Apache Airflow

## Prerequisites
- Docker and Docker Compose
- Python 3.10 or higher
- Git

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd FinalProject_DE_DigitalSkola
    ```

2. Set up the environment variables:
    Create a `.env` file in the root directory and add the necessary environment variables. Refer to the sample provided in the project.

3. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up Docker containers:
    ```sh
    docker-compose up -d
    ```

## Usage

### Running the Project

1. Ensure all services are running:
    ```sh
    docker-compose ps
    ```

2. Access the web interfaces:
    - Airflow: [http://localhost:8080](http://localhost:8080)
    - MongoDB: [http://localhost:27017](http://localhost:27017)
    - PostgreSQL: [http://localhost:5432](http://localhost:5432)

### Scheduling and Executing Tasks

- Tasks can be scheduled and managed using Apache Airflow. Access the Airflow UI and trigger the DAGs as required.

## Project Structure
```
FinalProject_DE_DigitalSkola/
├── .git/                    # Git version control directory
├── logs/                    # Log files
├── plugins/                 # Python scripts for data processing
│   ├── finnhub_loader.py
│   ├── finnhub_mongodb_loader.py
│   ├── mongodb_loader.py
│   ├── postgres_loader.py
│   ├── sentiment_analysis.py
│   ├── sentiment_analysis_loader.py
│   └── __pycache__/         # Compiled Python files
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Contributing
1. Fork the repository.
2. Create a new feature branch:
    ```sh
    git checkout -b feature/YourFeature
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/YourFeature
    ```
5. Open a pull request.
