import unittest
from utils import memory_data, time_data
from lab2.task10.src.tree import main, is_correct

class TestIsCorrect(unittest.TestCase):

    def test_empty_tree(self):
        self.assertTrue(is_correct(0, {}))

    def test_single_node(self):
        nodes = {1: (5, 0, 0)}
        self.assertTrue(is_correct(1, nodes))

    def test_valid_small_tree(self):
        nodes = {
            1: (2, 2, 3),
            2: (1, 0, 0),
            3: (3, 0, 0),
        }
        self.assertTrue(is_correct(3, nodes))

    def test_invalid_left_child_larger(self):
        nodes = {
            1: (3, 2, 0),
            2: (5, 0, 0),
        }
        self.assertFalse(is_correct(2, nodes))

    def test_invalid_right_child_smaller(self):
        nodes = {
            1: (4, 0, 2),
            2: (3, 0, 0),
        }
        self.assertFalse(is_correct(2, nodes))

    def test_duplicate_values(self):
        nodes = {
            1: (2, 0, 2),
            2: (2, 0, 0),
        }
        self.assertFalse(is_correct(2, nodes))

    def test_deep_valid_tree(self):
        nodes = {
            1: (10, 2, 5),
            2: (5, 3, 4),
            3: (1, 0, 0),
            4: (7, 0, 0),
            5: (15, 6, 0),
            6: (12, 0, 0),
        }
        self.assertTrue(is_correct(6, nodes))

    def test_deep_invalid_tree(self):
        nodes = {
            1: (10, 2, 5),
            2: (5, 3, 4),
            3: (1, 0, 0),
            4: (7, 0, 0),
            5: (15, 6, 0),
            6: (9, 0, 0),
        }
        self.assertFalse(is_correct(6, nodes))

    def test_chain_right_valid(self):
        nodes = {
            1: (1, 0, 2),
            2: (2, 0, 3),
            3: (3, 0, 4),
            4: (4, 0, 0),
        }
        self.assertTrue(is_correct(4, nodes))

    def test_chain_right_invalid(self):
        nodes = {
            1: (4, 0, 2),
            2: (3, 0, 3),
            3: (2, 0, 4),
            4: (1, 0, 0),
        }
        self.assertFalse(is_correct(4, nodes))

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
