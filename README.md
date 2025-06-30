# 📊 Automated Data Pipeline for Financial News Sentiment Analysis

![Untitled-2024-06-23-1930](https://github.com/andrewsuadnya/FinalProject_DE_DigitalSkola/assets/90898706/0dfb04d3-f428-4dfe-bf5b-6bf8bf9cdc8d)

## Project Overview

This project is part of the final assessment for the Data Engineering program at DigitalSkola. It implements an automated data pipeline that collects, analyzes, and stores financial news to provide sentiment insights for market monitoring. The pipeline integrates several tools:
- **Finnhub API**: To fetch news data.
- **MongoDB Atlas**: To store news data fetched from Finnhub.
- **PostgreSQL**: To store the sentiment analysis results of the news.
- **Apache Airflow**: To orchestrate and schedule tasks in the pipeline.

## 🔁 Pipeline Flow Summary

1. **Extract** news data from the Finnhub API.
2. **Load** data into MongoDB Atlas.
3. **Analyze** the sentiment of the news articles.
4. **Load** sentiment results into PostgreSQL.
5. **Orchestrate** all tasks using Airflow.

## Steps

1. **Sign Up for Finnhub**: [Finnhub API](https://finnhub.io/docs/api/symbol-search)
2. **Sign Up/Login to MongoDB Atlas**: Create a cluster or use an existing cluster: [MongoDB Atlas](https://cloud.mongodb.com)
3. **Configure Airflow with Docker Compose**: Use the provided [Airflow Docker Compose](https://shrib.com/#Phillip3yM6o5k) and save it to `docker-compose.yaml`.
4. **Create a New Database in PostgreSQL**: This will be used to load the output table.
5. **Write Python Code to Load News from Finnhub to MongoDB Atlas**: The scripts are located in the `plugins` directory.
6. **Write Python Code to Analyze News from MongoDB and Load it to PostgreSQL**: The analysis scripts are also in the `plugins` directory.
7. **Schedule the Tasks using Airflow DAG**: Manage and schedule steps 5 and 6 using Airflow.

## Directory Structure

- `docker-compose.yml`: Configuration for Docker Compose to set up the working environment.
- `README.md`: Project documentation.
- `requirements.txt`: List of Python dependencies needed for the project.
- `.git/`: Git repository configurations and hooks.
- `logs/`: Logs from the scheduler and DAG related to sentiment analysis.
- `plugins/`: Contains various Python scripts for loading data and performing sentiment analysis.

## Plugins Directory

- `finnhub_loader.py`: Script to load news data from Finnhub to MongoDB.
- `finnhub_mongodb_loader.py`: Additional loader script for Finnhub to MongoDB.
- `mongodb_loader.py`: Script to interact with MongoDB.
- `postgres_loader.py`: Script to load data into PostgreSQL.
- `sentiment_analysis.py`: Script to perform sentiment analysis on news data.
- `sentiment_analysis_loader.py`: Script to load sentiment analysis results into PostgreSQL.

## How to Run

1. Clone the repository.
2. Set up the environment using the `docker-compose.yml` file.
3. Install dependencies from `requirements.txt`.
4. Configure your Finnhub and MongoDB Atlas credentials in the respective scripts.
5. Run the Airflow scheduler and webserver.
6. Trigger the DAGs to start the data pipeline.

## Running the Pipeline
### Load Finnhub News into MongoDB
```bash
docker exec -it airflow_webserver bash
python /opt/airflow/plugins/finnhub_mongodb_loader.py
```
### Run Sentiment Analysis and Store in PostgreSQL
```bash
python /opt/airflow/plugins/sentiment_analysis_loader.py
```
---

## ✅ Validation
* Use a PostgreSQL client or CLI to verify records in the target table:
```bash
psql -h postgres -U airflow -d data_warehouse
```
---

## 📌 Notes
* Make sure to configure your Finnhub API key and MongoDB connection strings in the relevant plugin scripts.
* DAGs should be defined in Airflow to automate the full pipeline.
