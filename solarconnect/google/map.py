import pandas as pd
import requests

GOOGLE_MAP_URL = 'https://maps.googleapis.com/maps/api/geocode/json'


class GoogleMap(object):
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.dataframe = None
        self.report = None

    def get_response(self, address=None, components=None):
        api_key = self.api_key
        payload = {'address': address,
                   'components': components,
                   'key': api_key}
        response = requests.get(GOOGLE_MAP_URL, params=payload)
        data = response.json()
        if data.get(u'status') == 'OK':
            result = data.get(u'results')[0]
        else:
            result = None
        self.report = result
        return self

    def get_report(self):
        return self.report
