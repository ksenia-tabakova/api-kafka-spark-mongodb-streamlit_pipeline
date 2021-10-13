Kafka running as docker container was added to the pipeline (see [docker-compose file](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/Kafka/docker-compose-kafka.yml)).

One topic and one consumer were created to test if data flows through the pipeline correctly:
./kafka-topics.sh --create --topic fmi-ingestion-topic --bootstrap-server localhost:9092
./kafka-console-consumer.sh --topic fmi-ingestion-topic --bootstrap-server localhost:9092

Pipeline was tested with Postman.
