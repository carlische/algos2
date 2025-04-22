import unittest
from utils import memory_data, time_data
from lab4.task1.src.search import find_occurrences, main

class MyTestSearch(unittest.TestCase):
    def test_no_occurrences(self):
        self.assertEqual(find_occurrences("xyz", "abcdef"), [])

    def test_start_position(self):
        self.assertEqual(find_occurrences("abc", "abcxyz"), [1])

    def test_end_position(self):
        self.assertEqual(find_occurrences("yz", "xyz"), [2])

    def test_overlapping(self):
        self.assertEqual(find_occurrences("aa", "aaaa"), [1, 2, 3])

    def test_full_match(self):
        self.assertEqual(find_occurrences("abcd", "abcd"), [1])

    def test_empty_pattern(self):
        self.assertEqual(find_occurrences("", "abc"), [])

    def test_longer_pattern(self):
        self.assertEqual(find_occurrences("abcdef", "abc"), [])

    def test_case_sensitive(self):
        self.assertEqual(find_occurrences("Ab", "aBcAb"), [4])

    def test_should_check_time_data(self):
        expected_time = 2
        time = time_data(main)
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        expected_memory = 256
        current, peak = memory_data(main)
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)


if __name__ == '__main__':
    unittest.main()
