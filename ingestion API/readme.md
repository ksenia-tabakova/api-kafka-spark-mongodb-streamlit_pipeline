## Ingestion API

FastAPI framework was used to develop simple ingestion API [script)(https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/ingestion%20API/main.py). For this pipeline, a single POST method was created. 
API was tested with Postman (snippet is [here](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/ingestion%20API/postman-test-api-post.py)).

Once all is working correctly, app was moved to the container (see [docker file](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/blob/main/ingestion%20API/dockerfile)).
