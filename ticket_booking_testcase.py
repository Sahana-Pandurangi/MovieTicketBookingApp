__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

import unittest
from ticket_booking_lib import *
import unittest
import time

url_list_of_dates = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofshowdates"
url_list_of_shows = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofshows"
url_list_of_seats = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofshowseats"
url_add_seats = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/addshowseats"

headers_with_apikey = {'Content-type': 'application/json', 'Accept': 'application/json',
                       'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


# Testcases that test all the endpoints pertaining to ticket booking lambda interface.
class TicketBookingTestcases(unittest.TestCase):
    def get_list_of_dates_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_dates(url_list_of_dates, {'theater_id': 2, 'movie_id': 1},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Date")
        actual_val = response_json['date'][0]
        self.assertEqual(str(actual_val), '2022-06-01', "ERR: Failed to get the appropriate date")
        print("Checking Second Date")
        actual_val = response_json['date'][1]
        self.assertEqual(str(actual_val), "2022-06-02", "ERR: Failed to get the appropriate date")
        print("Checking Third Date")
        actual_val = response_json['date'][2]
        self.assertEqual(str(actual_val), "2022-06-03", "ERR: Failed to get the appropriate date")

    def get_list_of_dates_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_dates(url_list_of_dates,
                                                                {'theater_id': None, 'movie_id': None},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_dates_negative_test_two(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_dates(url_list_of_dates,
                                                                {'theater_id': 2, 'movie_id': None},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_dates_negative_test_three(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_dates(url_list_of_dates,
                                                                {'theater_id': None, 'movie_id': 1},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_shows_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_times(url_list_of_shows,
                                                                {'theater_id': 2, 'movie_id': 1,
                                                                 'show_date': '2022-06-01'},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Time")
        actual_val = response_json['shows'][0]["start_time"]
        self.assertEqual(str(actual_val), "12:30:00", "ERR: Failed to post the appropriate show time")
        print("Checking selected show id")
        actual_val = response_json['shows'][0]["show_id"]
        self.assertEqual(str(actual_val), "1", "ERR: Failed to post the appropriate show id")

    def get_list_of_shows_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_times(url_list_of_shows,
                                                                {'theater_id': 2, 'movie_id': 1, 'show_date': None},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_shows_negative_test_two(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_times(url_list_of_shows,
                                                                {'theater_id': 2, 'movie_id': None,
                                                                 'show_date': '2022-06-01'},
                                                                headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_shows_negative_test_three(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_show_times(url_list_of_shows,
                                                                {'theater_id': None, 'movie_id': None,
                                                                 'show_date': None}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_seats_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats, {'show_id': 6}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Seat")
        actual_val = response_json['seats'][0]['seat_row']
        self.assertEqual(str(actual_val), "B", "ERR: Failed to get the appropriate seat row")
        actual_val = response_json['seats'][0]['seat_number']
        self.assertEqual(str(actual_val), "12", "ERR: Failed to get the appropriate seat number")
        actual_val = response_json['seats'][0]['seat_type']
        self.assertEqual(str(actual_val), "Premium", "ERR: Failed to get the appropriate seat row")
        actual_val = response_json['seats'][0]['price']
        self.assertEqual(str(actual_val), "25", "ERR: Failed to get the appropriate seat number")

    def get_list_of_seats_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats, {'user_id': 1}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_seats_negative_test_two(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats, {'key': 6},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_seats_negative_test_three(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.get_seats(url_list_of_seats, {'show_id': None}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_seats_positive_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_add_seats,
                                                            params={'user_id': 1, 'show_id': 6, 'number_of_seats': 2,
                                                                    'seats_remaining': 3,
                                                                    'theater_room_id': 2},
                                                            json_val={'booked_seats': ["1", "2"]},
                                                            headers=headers_with_apikey)

        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['total_booking_cost']
        self.assertEqual(str(actual_val), "20", "ERR: Failed to post the appropriate seats")

    def post_selected_seats_negative_test_one(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_add_seats,
                                                            params={'user_id': None, 'show_id': None,
                                                                    'number_of_seats': None, 'seats_remaining': None,
                                                                    'theater_room_id': None},
                                                            json_val={'booked_seats': ["1", "2"]},
                                                            headers=headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_seats_negative_test_two(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_add_seats,
                                                            params={'user_id': 1, 'show_id': None, 'number_of_seats': 2,
                                                                    'seats_remaining': 3,
                                                                    'theater_room_id': 2},
                                                            json_val={'booked_seats': ["1", "2"]},
                                                            headers=headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_seats_negative_test_three(self):
        general_obj = TicketBooking()
        status_code, response_json = general_obj.post_seats(url_add_seats,
                                                            params={'user_id': None, 'show_id': None,
                                                                    'number_of_seats': None, 'seats_remaining': None,
                                                                    'theater_room_id': None},
                                                            json_val={'booked_seats': [None]},
                                                            headers=headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def tearDown(self):
        time.sleep(5)
