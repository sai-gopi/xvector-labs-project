# This file is for testing the code(unit-testing) the actual file is in xvector_labs_project.py file

from unittest import TestCase
import unittest
import json
import requests


class TestProject(TestCase):
    def test_get_records(self):
        self.response = requests.get('http://127.0.0.1:5000/dataset')
        self.assertTrue(self.response.json()['message'] == 'successful')

    def test_write_record(self):
        record = {'eid': 127, 'salary': 86000, 'age': 26}
        self.response = requests.post('http://127.0.0.1:5000/dataset', data=json.dumps(record))
        self.assertTrue(self.response.json()['message'] == 'successfully added')

    def test_filtered_value(self):
        col_name = 'age'
        operation = 'max'
        self.response = requests.post('http://127.0.0.1:5000/dataset/' + col_name + operation)
        self.assertTrue(self.response.json()['message'] == 'successful')

    def test__plotting(self):
        col_1 = 'salary'
        col_2 = 'age'
        self.response = requests.get('http://127.0.0.1:5000/dataset/' + col_1 + col_2)
        self.assertTrue(self.response.json()['message'] == 'output directed to other thread/process')


if __name__ == "__main__":
    unittest.main()
