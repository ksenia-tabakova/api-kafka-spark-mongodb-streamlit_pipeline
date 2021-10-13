import requests
import json

url = "http://127.0.0.1:8000/Measurement"

payload = json.dumps({
  "time_UTC": "10-10-2021 19:20:00",
  "station_name": "Kemi Ajos",
  "latitude": 65.67319,
  "longitude": 24.5152,
  "temperature_2m": 8.9,
  "wind_speed_10min": 8.7,
  "wind_gust_10min": 10.8,
  "wind_direction_10min": 200,
  "relative_humidity": 100,
  "dew_point_temperature": 8.9,
  "precipitation_amount_1h": None,
  "precipation_intensity_10min": None,
  "snow_depth": None,
  "pressure_at_sea_level": 1008.4,
  "horizontal_visibility": 15900,
  "cloud_amount": 8,
  "present_weather": 20
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
