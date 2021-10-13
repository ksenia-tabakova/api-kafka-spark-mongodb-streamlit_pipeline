import datetime as dt
from fmiopendata.wfs import download_stored_query
import pandas as pd
import requests

# Retrieve the latest hour of data from bounding box for Finland
end_time = dt.datetime.utcnow()
start_time = end_time - dt.timedelta(hours=1)

# Convert times to strings
start_time = start_time.isoformat(timespec="seconds") + 'Z'
end_time = end_time.isoformat(timespec="seconds") + 'Z'

#bounding box - we retrieve all stations from Finland
bbox = '18,55,35,75'

#Fetch weather observations
obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                            args=["bbox="+bbox,
                            "starttime="+start_time,
                            "endtime+"+end_time,
                            "timeseries=True"])

observations = obs.data
location_info = obs.location_metadata
#example_station = 'Kemi Ajos'

URL = 'http://localhost:80/Measurement'  #Place to send data - app run on container
#URL = 'http://localhost:80/Measurement' # app runs locally

short_names = ['times', 'station', 'latitude', 'longitude', 't2m', 'ws_10min', 'wg_10min', 'wd_10min', 'rh', 'td', 'r_1h', 'ri_10min', 'snow_aws', 'p_sea', 'vis', 'n_man', 'wawa']
column_names = ['time_UTC', 'station_name', 'latitude', 'longitude','temperature_2m', 'wind_speed_10min', 'wind_gust_10min', 'wind_direction_10min', 'relative_humidity', 'dew_point_temperature',
                'precipitation_amount_1h', 'precipitation_intensity_10min', 'snow_depth', 'pressure_at_sea_level', 'horizontal_visibility', 'cloud_amount', 'present_weather']

def get_station_data(station_dict, station_name, location_info):
# This function goes over data for one station and transform data to Pandas dataframe

    df = pd.DataFrame()
    
    for key in station_dict.keys():
        if key == "times":  #convert date to proper format
            df[key] = [dateobj.strftime("%d-%m-%Y %H:%M:%S") for dateobj in station_dict[key]]
        else:
            df[key] = station_dict[key]["values"]

    df['station'] = station_name  #add station name
    df['latitude'] = location_info['latitude']  #add latitude
    df['longitude'] = location_info['longitude']  #add longitude
    return(df)                

for station in observations.keys():  #go over every station in the retrieved data
    df = get_station_data(observations[station], station, location_info[station]) 
    df =df[short_names]  #sort columns
    df.columns=column_names  #rename columns
    for i in df.index:  #go over every row in the dataframe
        json_string = df.iloc[[i]].to_json(orient='records', lines=True).splitlines()  #convert it to json
        print(json_string[0])
        response = requests.post(URL, data=json_string[0])  #send data to API
        print(response)
