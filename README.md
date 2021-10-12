# api-kafka-spark-mongodb-streamlit_pipeline
## Purpose of the project

This project has several goals:

1. Read Finnish Meteorological Data Institute data on weather observations from Finnish stations
2. Create simple dta ingestion API in python with FastAPI
3. Use Apache Kafka to buffer incoming messages with observation methods
4. Use Spark to subscribe to Kafka
5. Stream with Spark messages to MongoDB
6. Query MongoDB and visualize data with the help of Streamlit
7. Overarching purpose - containerize everything down the pipelines staeting from ingestion app

All scripts are writen in Python.

The parts of the project were built gradually, "growing on layers" and can be roughly broken down to the following steps:
1. Write FMI data load script
2. Write ingestion API using FastAPI framework
3. Test it with Postman
4. Add kafka into the picture: kafka runs on container and we add production of kafka strings to ingestion API code. Create local producer and consumer. Test new setup with Postman.
6. Containerize Ingestion API app and test pipeline with Postman.
