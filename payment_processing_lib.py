__author__ = 'Sahana Pandurangi Raghavendra'
__author__ = 'Megana Reddy Boddam'

# importing api methods file that contain the GET and POST library code
from api_methods_lib import *

# Class that implements all libraries to test the API ends pertaining Payment Processing lambda service
class PaymentProcessing:

    def __init__(self):
        self.methods_api = Apimethods()

    # Function to test the API that posts booking cost back to the backend
    # input :
    # request_url / api endpoint to which request has to be sent
    # params: query string parameters that has to be sent with the API request
    # headers: headers that need to be added for that API
    #output : status code and api response in json format
    def post_booking_cost(self, request_url, params=None, headers=None):
        print("Posting the booking cost")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that returns the total cost of booked show and food/beverages
    # input :
    # 1. request_url / api endpoint to which request has to be sent
    # 2. params: query string parameters that has to be sent with the API request
    # 3. headers: headers that need to be added for that API
    # output: status code and api response in json format
    def get_booking_cost(self, request_url, params=None, headers=None):
        print("Getting the total cost of booked show and food/beverages")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json

    # Function to test the API that returns the list of tickets booked by the customer
    # input :
    # 1. request_url / api endpoint to which request has to be sent
    # 2. params: query string parameters that has to be sent with the API request
    # 3. headers: headers that need to be added for that API
    # output: status code and api response in json format
    def get_tickets(self, request_url, params=None, headers=None):
        print("Getting the list of booked tickets")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        print(response_json)
        return status_code, response_json
