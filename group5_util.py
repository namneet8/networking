# author : Group 5
# date   : August 3, 2024
# filename: group5_util.py

from random import uniform
from time import asctime
from json import dumps

class Util:
    def __init__(self):
        self.start_id = 100

    def get_json_data(self):
        """Creates and returns a structured data dictionary with weather information."""
        self.start_id += 1  # Increment ID for each payload
        
        data = {
            'id': self.start_id,  # Sequence number
            'location': 'Toronto',  # Location
            'timestamp': asctime(),  # Time this was generated
            'temperature': round(uniform(-10, 35), 2),  # Temperature (in Celsius)
            'humidity': round(uniform(20, 100), 2),  # Humidity
            'wind_speed': round(uniform(0, 20), 2),  # Wind speed in m/s
            'precipitation': round(uniform(0, 100), 2),  # Precipitation in mm
            'uv_index': round(uniform(0, 11), 2),  # UV index
            'visibility': round(uniform(1, 10), 2)  # Visibility in km
        }

        return data

def print_data(data):
    """Prints the structured data in a human-readable format."""
    print("ID:", data['id'])
    print("Location:", data['location'])
    print("Timestamp:", data['timestamp'])
    print("Temperature:", data['temperature'], "°C")
    print("Humidity:", data['humidity'], "%")
    print("Wind Speed:", data['wind_speed'], "m/s")
    print("Precipitation:", data['precipitation'], "mm")
    print("UV Index:", data['uv_index'])
    print("Visibility:", data['visibility'], "km")
    print("-" * 40)








