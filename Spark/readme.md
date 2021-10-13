## Spark in brief

Apache Spark was set to run as container and using jupyter-lab (see [docker-compose file](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/Spark/docker-compose-kafka-spark.yml)).

Spark is subscribed to fmi-ingestion-topic, reads records from there, processes them to json and send to the MongoDB. ([Script](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/Spark/spark-stream-mongodb.ipynb))
