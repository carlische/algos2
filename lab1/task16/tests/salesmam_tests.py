import unittest
from utils import memory_data, time_data
from lab1.task16.src.salesman import main, salesman


class TestSalesman(unittest.TestCase):
    def test_should_work_only_one_city(self):
        # given
        n = 1
        array = [0]
        expected_result = (0, [1])

        # when
        result = salesman(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_two_cities(self):
        # given
        n = 2
        array = [[0, 5], [5, 0]]
        expected_result = (5, [2, 1])

        # when
        result = salesman(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_three_cities(self):
        # given
        n = 3
        array = [[0, 1, 2], [1, 0, 3], [2, 3, 0]]
        expected_result = (3, [3, 1, 2])

        # when
        result = salesman(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_zero_distance(self):
        # given
        n = 4
        array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        expected_result = (0, [4, 3, 2, 1])

        # when
        result = salesman(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_work_with_thirteen_cities(self):
        # given
        n = 13
        array = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]]
        expected_result = (12, [13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        # when
        result = salesman(n, array)

        # then
        self.assertEqual(result, expected_result)

    def test_should_check_time_data(self):
        # given
        expected_time = 2

        # when
        time = time_data(main)

        # then
        self.assertLess(time, expected_time)

    def test_should_check_memory_data(self):
        # given
        expected_memory = 256

        # when
        current, peak = memory_data(main)

        # then
        self.assertLess(current, expected_memory)
        self.assertLess(peak, expected_memory)

if __name__ == "__main__":
    unittest.main()
