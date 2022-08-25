__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

from payment_processing_lib import *
import unittest
import time

url_booking_cost = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/bookingcost"
url_list_of_tickets = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoftickets"

headers_with_api_key = {'Content-type': 'application/json', 'Accept': 'application/json',
                        'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


# Testcases that test all the endpoints pertaining to payment processing lambda interfaces.
class PaymentProcessingTestcases(unittest.TestCase):

    def post_booking_cost_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': 8},
                                                                   headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['total_cost']
        self.assertEqual(str(actual_val), "140", "ERR: Failed to post the appropriate booking cost")

    def post_booking_cost_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': "abc"},
                                                                   headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_booking_cost_negative_test_two(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': "123j"},
                                                                   headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_booking_cost_negative_test_three(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.post_booking_cost(url_booking_cost, {'booking_id': None},
                                                                   headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_booking_cost_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': 1},
                                                                  headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['total_cost']
        self.assertEqual(str(actual_val), "4", "ERR: Failed to get the appropriate booking cost")
        actual_val = response_json['seat_cost']
        self.assertEqual(str(actual_val), "4", "ERR: Failed to get the appropriate booking cost")
        actual_val = response_json['food_cost']
        self.assertEqual(str(actual_val), "0", "ERR: Failed to get the appropriate booking cost")

    def get_booking_cost_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': "abc"},
                                                                  headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_booking_cost_negative_test_two(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': "123j"},
                                                                  headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_booking_cost_negative_test_three(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_booking_cost(url_booking_cost, {'booking_id': None},
                                                                  headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_tickets_positive_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': 1},
                                                             headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        self.check_ticket_positive_test_one(response_json)

    def check_ticket_positive_test_one(self, response_json):
        actual_val = response_json['city_name']
        self.assertEqual(str(actual_val), "Kirkland", "ERR: Failed to get the appropriate ticket")
        print("Checking city name on ticket")
        actual_val = response_json['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to get the appropriate ticket")
        print("Checking theater name on ticket")
        actual_val = response_json['movie_name']
        self.assertEqual(str(actual_val), "Pushpa: The Rise - Part 1", "ERR: Failed to get the appropriate ticket")
        print("Checking movie name on ticket")
        actual_val = response_json['show_date']
        self.assertEqual(str(actual_val), "Thu Jun 02", "ERR: Failed to get the appropriate ticket")
        print("Checking show date on ticket")
        actual_val = response_json['start_time']
        self.assertEqual(str(actual_val), "12:30:00", "ERR: Failed to get the appropriate ticket")
        print("Checking start time on ticket")
        actual_val = response_json['end_time']
        self.assertEqual(str(actual_val), "15:29:00", "ERR: Failed to get the appropriate ticket")
        print("Checking end time on ticket")
        actual_val = response_json['room_name']
        self.assertEqual(str(actual_val), "Screen Room C", "ERR: Failed to get the appropriate ticket")
        print("Checking room  on ticket")
        actual_val = response_json['cost']
        self.assertEqual(str(actual_val), "4", "ERR: Failed to get the appropriate ticket")
        print("Checking cost on ticket")

    def get_list_of_tickets_negative_test_one(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': "abc"},
                                                             headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_tickets_negative_test_two(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': "123j"},
                                                             headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_tickets_negative_test_three(self):
        general_obj = PaymentProcessing()
        status_code, response_json = general_obj.get_tickets(url_list_of_tickets, {'booking_id': None},
                                                             headers_with_api_key)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def tearDown(self):
        time.sleep(5)
