import unittest
from translator import french_to_english, english_to_french
from ibm_cloud_sdk_core.api_exception import ApiException

class TestEnglishToFrench(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_null_input(self):
        self.assertRaises(ApiException, english_to_french, '')

class TestFrenchToEnglish(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
    def test_null_input(self):
        self.assertRaises(ApiException, french_to_english, '')

unittest.main()