__author__ = 'Sahana Pandurangi Raghavendra', 'Megana Reddy Boddam'

import unittest
from payment_processing_testcase import *


def suite():
    suite = unittest.TestSuite()
    testcases = [
        "post_booking_cost_positive_test_one",
        "get_booking_cost_positive_test_one",
        "post_booking_cost_negative_test_one",
        "get_booking_cost_negative_test_one",
        "post_booking_cost_negative_test_two",
        "get_booking_cost_negative_test_two",
        "post_booking_cost_negative_test_three",
        "get_booking_cost_negative_test_three",
        "get_list_of_tickets_positive_test_one",
        "get_list_of_tickets_negative_test_one",
        "get_list_of_tickets_negative_test_two",
        "get_list_of_tickets_negative_test_three",
    ]
    for i in range(len(testcases)):
        suite.addTest(PaymentProcessingTestcases(testcases[i]))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
