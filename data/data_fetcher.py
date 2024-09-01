import requests

class TrackingAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.17track.net/track/v2.2/gettrackinfo'

    def fetch_tracking_info(self, tracking_numbers, carrier_codes):
        """Fetch tracking information from the API."""
        headers = {
            '17token': self.api_key,
            'Content-Type': 'application/json'
        }
        data = [{'number': num, 'carrier': carrier_codes.get(num, None)} for num in tracking_numbers]
        response = requests.post(self.base_url, json=data, headers=headers)
        return response.json()
