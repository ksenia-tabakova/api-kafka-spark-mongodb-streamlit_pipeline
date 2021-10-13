from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder #to turn classes to jsons
from fastapi.responses import JSONResponse
from typing import Optional

import json #needed for json.dumps
from pydantic import BaseModel
import kafka

# Create class(API schema) for the JSON
# data gets ingested as a string and them validated before writing
# Missing observations are expected (due to the instrument failure or absense of natural phenomena, such as rain or snowcover)
class Measurement(BaseModel):
    time_UTC: str
    station_name: str
    latitude: float
    longitude: float
    temperature_2m: Optional[float] = None
    wind_speed_10min: Optional[float] = None
    wind_gust_10min: Optional[float] = None
    wind_direction_10min: Optional[float] = None
    relative_humidity: Optional[float] = None
    dew_point_temperature: Optional[float] = None
    precipitation_amount_1h: Optional[float] = None
    precipitation_intensity_10min: Optional[float] = None
    snow_depth: Optional[float] = None
    pressure_at_sea_level: Optional[float] = None
    horizontal_visibility: Optional[float] = None
    cloud_amount: Optional[float] = None
    present_weather: Optional[float] = None

app = FastAPI()

#Base URL
@app.get("/")
async def root():
    return {"message": "Hello World!"}

#Add a new measurement
@app.post("/Measurement")
async def post_measurement_item(item: Measurement):
    print("Message received")
    try:
        json_of_item = jsonable_encoder(item)  #encode incoming record

        #Dump json out as string
        json_as_string = json.dumps(json_of_item)
        print(json_as_string)

        #Produce the string
        produce_kafka_string(json_as_string)
        return JSONResponse(content=json_of_item, status_code = 201)
    except ValueError:
        return JSONResponse(content=jsonable_encoder(item), status_code = 401)

def produce_kafka_string(json_as_string):
    # Create a producer
    #producer = kafka.KafkaProducer(bootstrap_servers='localhost:9093', acks=1) #before container
    producer = kafka.KafkaProducer(bootstrap_servers='kafka:9092', acks=1) #app in the container
    #Write string as bytes because Kafka needs it
    producer.send('fmi-ingestion-topic', bytes(json_as_string,'utf-8'))
    producer.flush() #flush so that all messages are there
