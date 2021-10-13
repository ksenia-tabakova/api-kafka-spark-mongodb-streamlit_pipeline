# api-kafka-spark-mongodb-streamlit_pipeline
## Purpose of the project

This project has several goals:

1. Read [Finnish Meteorological Data Institute data](https://en.ilmatieteenlaitos.fi/open-data) on weather observations from Finnish stations
2. Create simple dta ingestion API in python with FastAPI
3. Use Apache Kafka to buffer incoming messages with observation methods
4. Use Spark to subscribe to Kafka
5. Stream with Spark messages to MongoDB
6. Query MongoDB and visualize data with the help of Streamlit
7. Overarching purpose - containerize everything down the pipelines staeting from ingestion app

All scripts are writen in Python.

## Steps to create pipeline

The parts of the project were built gradually as if "growing on layers" and can be roughly broken down to the following steps:
1. Write FMI data load script [tba](tba)
2. Write ingestion API using FastAPI framework; test it with Postman [tba](tba)
3. Add Kafka to the pipeline kafka runs on container and production of kafka strings to ingestion API code added. Create local producer and consumer. Test new setup with Postman. [tba](tba)
5. Containerize Ingestion API app and test pipeline with Postman. [tba](tba)
6. Add Spark to the pipeline: spark runs on container using jupyterlab. Start Spark session, subscribe to the kafka topic to listen to the messages. Create second topic on Kafka for Spark output to test that Spark is working correctly.[tba](tba)
7. Add MongoDB to the pipeline. MongoDB runs on container. Add to Spark script data processing and write to MongoDB database. Test that data is recorded correctly. [tba](tba)
8. Now when all parts of pipeline work correctly, database can be populated with data. [tba](tba)
9. Add Streamlit to the pipeline: streamlit connects to MongoDB and queries data. Interactive dashboard is created to display queried data. [tba](tba)
