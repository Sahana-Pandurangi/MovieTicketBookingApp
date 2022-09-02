__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'
from api_methods_lib import *


class TicketBooking:

    def __init__(self):
        self.methods_api = Apimethods()

    def get_show_dates(self, request_url, params=None, headers=None):
        print("Getting the list of available dates for viewing the selected movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_show_date(self, request_url, params=None, headers=None):
        print("Posting the selected date")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_show_times(self, request_url, params=None, headers=None):
        print("Getting the list of available times for viewing the selected movie")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_show_times(self, request_url, params=None, headers=None):
        print("Posting the selected time")
        response = self.methods_api.post(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def get_seats(self, request_url, params=None, headers=None):
        print("Getting the list of available seats")
        response = self.methods_api.get(request_url, params=params, headers=headers)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json

    def post_seats(self, request_url, params=None, headers=None, json_val= None):
        print("Posting the selected seats")
        response = self.methods_api.post(request_url, params=params, headers=headers, json_val=json_val)
        status_code = response.status_code
        response_json = response.json()
        logging.Logger(response_json)
        return status_code, response_json
