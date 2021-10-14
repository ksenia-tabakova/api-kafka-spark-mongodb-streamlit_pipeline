## Data used for this project
Finnish Meteorological Institute (FMI) has its dataset publicly available. FMI has written python library [fmiopendata](https://github.com/pnuu/fmiopendata) that enables easy access to the data. 
For this project I have decided to use weather observations data, and it includes observations on:
\['Air temperature','Cloud amount', 'Dew-point temperature', 'Gust speed', 'Horizontal visibility', 'Precipitation amount',
'Precipitation intensity', 'Present weather (auto)', 'Pressure (msl)', 'Relative humidity', 'Snow depth', 'Wind direction', 'Wind speed'\]

Observations for the last hour from Finnish weather stations is retrieved and processed to be in form of json strings.
Once data is cleared and ready, it is sent to the [ingestion API](https://github.com/ksenia-tabakova/api-kafka-spark-mongodb-streamlit_pipeline/tree/main/ingestion%20API).
