__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

# importing api methods file that contain the GET and POST library code
from api_methods_lib import *


# Class that implements all libraries to test the API ends pertaining Foodbooking lambda service
class FoodBooking:

    def __init__(self):
        self.methods_api = Apimethods()

    # Function to test the API that queries the database for a list avaliable
    # food items for consumption during movie
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def get_list_of_food(self, request_url, params=None, headers=None):
        print("Getting the list of available food and beverages for consumption during movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that posts the selected food and beverages by the customer
    # input : url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    def post_food(self, request_url, params=None, headers=None):
        print("Posting the selected food and beverages")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json
