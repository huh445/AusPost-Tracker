import requests

class APIHandler:
    def __init__(self, api_key):
        self.api_key = api_key

    def post_request(self, url, data):
        """Send a POST request to the API."""
        headers = {
            '17token': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.post(url, json=data, headers=headers)
        return response.json()
