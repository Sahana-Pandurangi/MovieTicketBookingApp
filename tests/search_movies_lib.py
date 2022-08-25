__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

from requests import post
from api_methods_lib import *


class SearchMovies:

    def __init__(self):
        self.methods_api = Apimethods()

    def get_user(self, request_url, params=None, headers=None):
        print("Getting the user details")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_user(self, request_url, params=None, headers=None):
        print("Posting the user details city")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_cities(self, request_url, params=None, headers=None):
        print("Getting the list of cities in USA")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_city(self, request_url, params=None, headers=None):
        print("Posting the selected city")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_theaters(self, request_url, params=None, headers=None):
        print("Getting the list of theaters in the city")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_theater(self, request_url, params=None, headers=None):
        print("Posting the selected theater")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_movies(self, request_url, params=None, headers=None):
        print("Getting the list of movies in the theater")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_movie(self, request_url, params=None, headers=None):
        print("Posting the selected movie")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json
