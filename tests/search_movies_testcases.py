__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

import unittest
from search_movies_lib import *
import time

url_add_new_user = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/addnewuser"
url_get_user = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/getuser"
url_list_of_cities = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofcities"
url_list_of_theaters = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listoftheaters"
url_list_of_movies = "https://9qhi5gewy6.execute-api.us-east-1.amazonaws.com/prod/listofmovies"

headers_with_apikey = {'Content-type': 'application/json', 'Accept': 'application/json',
                       'x-api-key': 'ynbWkSO7m32Mk64vd2d7NaD6VyYm8D1fH18A01O9'}


# Testcases that test all the endpoints pertaining to search movies lambda interface.
class SearchMoviesTestcases(unittest.TestCase):
    def get_user_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_user(url_get_user, {'user_id': 1}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking User ID")
        actual_val = response_json['user']['user_id']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to get the appropriate user ID")
        print("Checking User First Name")
        actual_val = response_json['user']['first_name']
        self.assertEqual(str(actual_val), "Jane", "ERR: Failed to get the appropriate user first name")
        print("Checking User Second Name")
        actual_val = response_json['user']['second_name']
        self.assertEqual(str(actual_val), "Austen", "ERR: Failed to get the appropriate user second name")
        print("Checking User Email")
        actual_val = response_json['user']['email']
        self.assertEqual(str(actual_val), "jane.austen@gmail.com", "ERR: Failed to get the appropriate user email")
        print("Checking User Phone")
        actual_val = response_json['user']['phone']
        self.assertEqual(str(actual_val), "2147483647", "ERR: Failed to get the appropriate user phone number")

    def get_user_positive_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_user(url_get_user, {'user_id': "1"}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking User ID")
        actual_val = response_json['user']['user_id']
        self.assertEqual(str(actual_val), "1", "ERR: Failed to get the appropriate user ID")
        print("Checking User First Name")
        actual_val = response_json['user']['first_name']
        self.assertEqual(str(actual_val), "Jane", "ERR: Failed to get the appropriate user first name")
        print("Checking User Second Name")
        actual_val = response_json['user']['second_name']
        self.assertEqual(str(actual_val), "Austen", "ERR: Failed to get the appropriate user second name")
        print("Checking User Email")
        actual_val = response_json['user']['email']
        self.assertEqual(str(actual_val), "jane.austen@gmail.com", "ERR: Failed to get the appropriate user email")
        print("Checking User Phone")
        actual_val = response_json['user']['phone']
        self.assertEqual(str(actual_val), "2147483647", "ERR: Failed to get the appropriate user phone number")

    def get_user_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_user(url_get_user, {},
                                                          headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_user_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_user(url_get_user, {'theater_id': "12abc"},
                                                          headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_user_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_user(url_get_user, {'user_id': None},
                                                          headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_add_new_user_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_user(url_add_new_user,
                                                           {'first_name': "Jane", 'second_name': "Austen",
                                                            'email': "jane.austen@gmail.com", 'phone': "2380942358"},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Sucessfully added the user to the database",
                         "ERR: Failed to post the appropriate user")

    def post_add_new_user_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_user(url_add_new_user, {},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_cities_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': 1}, headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First City")
        actual_val = response_json['city'][0]['city_name']
        self.assertEqual(str(actual_val), "Seattle", "ERR: Failed to get the appropriate city")
        print("Checking Second City")
        actual_val = response_json['city'][1]['city_name']
        self.assertEqual(str(actual_val), "Universal City", "ERR: Failed to get the appropriate city")
        print("Checking Third City")
        actual_val = response_json['city'][2]['city_name']
        self.assertEqual(str(actual_val), "Kirkland", "ERR: Failed to get the appropriate city")
        print("Checking Fourth City")
        actual_val = response_json['city'][3]['city_name']
        self.assertEqual(str(actual_val), "Redmond", "ERR: Failed to get the appropriate city")

    def get_list_of_cities_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': "abc"},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_cities_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': None},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_cities_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_cities(url_list_of_cities, {'user_id': "99999999ye"},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_city_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': 1, 'city_code': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['city'][0]['city_name']
        self.assertEqual(str(actual_val), "Seattle", "ERR: Failed to post the appropriate city")

    def post_selected_city_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': 1, 'city_code': "abc"},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_city_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': "abc", 'city_code': 1},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_city_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_city(url_list_of_cities, {'user_id': "abc", 'city_code': "abc"},
                                                           headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_theaters_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': 1},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Theater")
        actual_val = response_json['theater'][0]['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to get the appropriate theater")
        print("Checking Second Theater")
        actual_val = response_json['theater'][1]['theater_name']
        self.assertEqual(str(actual_val), "Lincoln Memorial Theater", "ERR: Failed to get the appropriate theater")
        print("Checking Third Theater")
        actual_val = response_json['theater'][2]['theater_name']
        self.assertEqual(str(actual_val), "Regal", "ERR: Failed to get the appropriate theater")

    def get_list_of_theaters_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': "abc"},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_theaters_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': 1, 'city_code': 'AB56'},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_theaters_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_theaters(url_list_of_theaters, {'user_id': "abc", 'city_code': 1},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_theater_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': 1, 'theater_id': 1},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        actual_val = response_json['theater'][0]['theater_name']
        self.assertEqual(str(actual_val), "Cinemark", "ERR: Failed to post the appropriate city")

    def post_selected_theater_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': 1, 'theater_id': "abc"},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_theater_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': "abc", 'theater_id': "abc"},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def post_selected_theater_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.post_theater(url_list_of_theaters,
                                                              {'user_id': None, 'theater_id': None},
                                                              headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_movies_positive_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': 1, 'theater_id': 2},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 200)
        print(str(response_json))
        print("Checking First Movie")
        actual_val = response_json['movie'][0]['name']
        self.assertEqual(str(actual_val), "Top Gun: Maverick", "ERR: Failed to get the appropriate movie")
        print("Checking Second Movie")
        actual_val = response_json['movie'][1]['name']
        self.assertEqual(str(actual_val), "Pushpa: The Rise - Part 1", "ERR: Failed to get the appropriate movie")

    def get_list_of_movies_negative_test_one(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': 1, 'theater_id': 'abc'},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_movies_negative_test_two(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': 'abc', 'theater_id': 1},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def get_list_of_movies_negative_test_three(self):
        general_obj = SearchMovies()
        status_code, response_json = general_obj.get_movies(url_list_of_movies,
                                                            {'user_id': None, 'theater_id': None},
                                                            headers_with_apikey)
        print(status_code)
        self.assertEqual(status_code, 400)
        print(str(response_json))
        actual_val = response_json['message']
        self.assertEqual(str(actual_val), "Invalid Input", "ERR: Failed to get the appropriate negative response")

    def tearDown(self):
        time.sleep(5)
