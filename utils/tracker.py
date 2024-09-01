import os
import requests

class Tracker:
    def __init__(self):
        self.api_key = os.getenv('TRACKER_API_KEY')
        if not self.api_key:
            raise ValueError("API key not found in environment variables.")
        self.api_url = 'https://api.17track.net/track/v2.2/gettrackinfo'

    def get_tracking_info(self, tracking_numbers, carrier_codes):
        print(f"Carrier Codes: {carrier_codes}")  # Debugging line
        headers = {
            '17token': self.api_key,
            'Content-Type': 'application/json'
        }
        data = [{'number': num, 'carrier': carrier_codes.get(num, None)} for num in tracking_numbers]
        print(f"Request Data: {data}")  # Debugging line
        response = requests.post(self.api_url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()


    def get_carrier_name(self, carrier_code):
        # Adjust this mapping as necessary
        carrier_names = {
            1151: 'Australia Post',
            # Add other carriers as needed
        }
        return carrier_names.get(carrier_code, 'Unknown Carrier')
