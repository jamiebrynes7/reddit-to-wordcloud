import unittest

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

if __name__ == "__main__":
    unittest.main()