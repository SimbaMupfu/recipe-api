from django.test import TestCase
from app.calc import add

class CalcTests(TestCase):

    def test_add_numbers(self):
        """test that two numbers are being added"""
        self.assertEqual(add(3, 8), 11)