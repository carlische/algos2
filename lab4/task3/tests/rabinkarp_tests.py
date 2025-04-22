import unittest
from utils import memory_data, time_data
from lab4.task3.src.rabinkarp import search_pattern_in_text, main

class TestSearchPatternInText(unittest.TestCase):
    def test_single_occurrence(self):
        text = "hello world"
        pattern = "world"
        result = search_pattern_in_text(pattern, text)
        self.assertEqual(result, [7])

    def test_multiple_occurrences(self):
        text = "ababcabcab"
        pattern = "abc"
        result = search_pattern_in_text(pattern, text)
        self.assertEqual(result, [3, 6])

    def test_no_occurrences(self):
        text = "abcdefgh"
        pattern = "xyz"
        result = search_pattern_in_text(pattern, text)
        self.assertEqual(result, [])

    def test_empty_pattern(self):
        text = "anything"
        pattern = ""
        result = search_pattern_in_text(pattern, text)
        self.assertEqual(result, [])

    def test_text_shorter_than_pattern(self):
        text = "short"
        pattern = "longerpattern"
        result = search_pattern_in_text(pattern, text)
        self.assertEqual(result, [])

    def test_should_check_time_data(self):
        expected_time = 2
        time = time_data(main)
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        expected_memory = 256
        current, peak = memory_data(main)
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)

if __name__ == "__main__":
    unittest.main()