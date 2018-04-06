import unittest
import time

import requests

from common_lib import generate_frequency_map

class TestRedditToWordcloud(unittest.TestCase):

    frequency_map_test = ["This is a test of the...", "frequency generation operation!", "It should IGNORE caps and punctuatio.n", "Frequency generation is cool!", "test test should wow"]
    filtered_words_test = {"a", "is", "and"}
    frequency_map_expected_result = {
        "this": 1,
        "test": 3,
        "of": 1,
        "the": 1,
        "frequency": 2,
        "generation": 2,
        "operation": 1,
        "it": 1,
        "should": 2,
        "ignore": 1,
        "caps": 1,
        "punctuation": 1,
        "cool": 1,
        "wow": 1
    }

    def test_generate_frequency_map(self):
        frequency_map = generate_frequency_map(self.frequency_map_test, self.filtered_words_test)
        print(frequency_map == self.frequency_map_expected_result)
        self.assertDictEqual(frequency_map, self.frequency_map_expected_result)


    aws_frontend_url = "https://28j7achrh2.execute-api.eu-west-2.amazonaws.com/production/reddit-to-wordcloud-frontend"
    aws_polling_url = "https://ge2puhouaa.execute-api.eu-west-2.amazonaws.com/production/reddit-to-wordcloud-polling"

    def test_aws_lambda_chain(self):
        r = requests.post(self.aws_frontend_url, json={
            "url": "https://www.reddit.com/r/reddevils/comments/86t6fy/european_night_attendance_high_for_city/",
            "wordcloud_settings": {

            }
        })
        self.assertEqual(r.status_code, 200)
        tag = r.json()["db_tag"]
        
        result = False
        while not result:
            r = requests.post(self.aws_polling_url, json={
                "db_tag": tag
            })

            self.assertEqual(r.status_code, 200)

            status = r.json()["status"]
            if status == "done":
                self.assertEqual(True, True)
                result = True
            elif status == "error":
                self.assertEqual(False, True)
                result = True
            
            time.sleep(3)

if __name__ == "__main__":
    unittest.main()