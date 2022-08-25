__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

from food_booking_lib import *
import unittest
import time

# urls / API endpoints used by food booking lambda service
url_list_of_food = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoffood"

# headers
headers_with_apikey = {'Content-type': 'application/json', 'Accept': 'application/json',
                       'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


# Testcases that test all the endpoints pertaining to food booking lambda interfaces.
class FoodBookingTestcases(unittest.TestCase):

    def get_list_of_food_positive_test_one(self):
        print("API listOfFood: GET: Test Case 1")
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food, {'user_id': 1, 'theater_id': 1},
                                                                  headers_with_apikey)
        print("status code is: " + str(status_code))
        print(self.assertEqual(status_code, 200))
        print("the response is: " + str(response_json))

        actual_val = response_json['food'][0]['food_name']
        print("Checking First Food " + str(actual_val))
        print(self.assertEqual(str(actual_val), "Small Butter Popcorn", "ERR: Failed to get appropriate food"))

        actual_val = response_json['food'][1]['food_name']
        print("Checking Second Food " + str(actual_val))
        print(self.assertEqual(str(actual_val), "Medium Butter Popcorn", "ERR: Failed to get appropriate food"))

        actual_val = response_json['food'][2]['food_name']
        print("Checking Third Food " + str(actual_val))
        print(self.assertEqual(str(actual_val), "Large Butter Popcorn", "ERR: Failed to get appropriate food"))

    def get_list_of_food_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food, {'user_id': 1, 'theater_id': "abc"},
                                                                  headers_with_apikey)
        print("status code is: " + str(status_code))
        print(self.assertEqual(status_code, 400))
        print(str(response_json))
        print(self.assertEqual(str(response_json['message']), "Invalid Input",
                               "ERR: Failed to get the appropriate negative response"))

    def get_list_of_food_negative_test_two(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food,
                                                                  {'user_id': 1, 'theater_id': "123b"},
                                                                  headers_with_apikey)
        print("status code is: " + str(status_code))
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_food_negative_test_three(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.get_list_of_food(url_list_of_food, {'user_id': 1, 'theater_id': None},
                                                                  headers_with_apikey)
        print("status code is: " + str(status_code))
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_food_positive_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food,
                                                           {'user_id': 1, 'booking_id': 1, 'food_id': 1, 'quantity': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Sucess", "ERR: Failed to post the appropriate food")

    def post_selected_food_negative_test_one(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food, {'user_id': 1, 'booking_id': 1,
                                                                              'food_id': "abc", 'quantity': "abc"},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_food_negative_test_two(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food, {'user_id': 1, 'booking_id': 1,
                                                                              'food_id': "abc", 'quantity': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_food_negative_test_three(self):
        general_obj = FoodBooking()
        status_code, response_json = general_obj.post_food(url_list_of_food, {'user_id': 1, 'booking_id': 1,
                                                                              'food_id': None, 'quantity': None},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def tearDown(self):
        time.sleep(2)
