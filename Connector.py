import json
from abc import abstractmethod

import requests

from DataModels import ConnectorResult
from SubProcessInputOutputHandler import SubProcessInputOutputHandler


class Connector(object):

    def __init__(self, api_key, url):

        self.api_key = api_key
        self.url = url
        self.io_mgr = SubProcessInputOutputHandler()
        self.connector_params = self.io_mgr.connector_params
        self.connector_result = ConnectorResult()

    def request_data_from_api(self, data):

        """
        This method gets the data from the api.
        :param data: the current data we wish to get from the api
        :return: the response of the request in a json format
        """
        try:
            params = {'apikey': self.api_key, 'resource': data, 'scan': 1}
            response = requests.get(self.url, params=params)
            response_json = json.loads(response.content)

        except:
            print("There was a problem with the response.")

        return response_json

    @abstractmethod
    def handle_response(self, response_json):
        """
        This method handles the response, process it, and saves it to the connector result.
        :param response_json: the response from the request in a json format
        :return: None
        """
        pass
