__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

"""
This is a library file that implements the post and get methods that are used for API requests
The python requests library is used to make API requests. 
The json library is used to convert the python object into json string
"""

import requests
from urllib import *
import json
import logging

default_headers = {'Content-type': 'application/json', 'Accept': 'application/json',
                   'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


class Apimethods:
    """
    The post method is used to send POST API request to the API gateway hosted on AWS cloud.
    Input parameters are as follows:
    1. url: The url to which API requests are sent.
    2. json_val = the data that must be sent in the post body
    3. params: The query string parameters that need to be sent along with API request
    4. files: The files that need to be sent in the POST request
    5. headers: The headers for the API request. That mainly contain the content type and api key
    Output:
    response: JSON response for the API request.
    """

    def post(self, url, json_val=None, params=None, files=None, headers=None):
        if headers is None:
            headers = default_headers
        if files is None:
            response = requests.post(url, data=json.dumps(json_val), params=params, files=files,
                                     headers=headers, verify=True)
        else:
            response = requests.post(url, params=params, files=files, verify=True)
        return response

    """
    The get method is used to send GET API request to the API gateway hosted on AWS cloud.
    Input parameters are as follows:
    1. url: The url to which API requests are sent.
    2. params: The query string parameters that need to be sent along with API request
    3. headers: The headers for the API request that mainly contain the content type and api key
    Output: 
    response: JSON response for the API request.
    """

    def get(self, url, params=None, headers=None):
        if headers is None:
            headers = default_headers
        response = requests.request("GET", url, params=params, headers=headers, verify=True)
        return response
