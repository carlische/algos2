import unittest
from utils import memory_data, time_data
from lab3.task12.src.colormaze import build_graph, process_path, main

class TestColorMaze(unittest.TestCase):

    def test_build_graph(self):
        """Тестирование построения графа"""
        corridors = [(1, 2, 1), (2, 3, 2)]
        graph = build_graph(3, 2, corridors)

        self.assertEqual(graph[1][1], 2)
        self.assertEqual(graph[2][1], 1)
        self.assertEqual(graph[2][2], 3)
        self.assertEqual(graph[3][2], 2)
        self.assertEqual(len(graph), 4)  # комнаты 0-3

    def test_process_path_valid(self):
        """Тестирование корректного пути"""
        graph = [None, {1: 2}, {1: 1, 2: 3}, {2: 2}]
        self.assertEqual(process_path(graph, [1, 2]), 3)

    def test_process_path_invalid(self):
        """Тестирование некорректного пути"""
        graph = [None, {1: 2}, {1: 1, 2: 3}, {2: 2}]
        self.assertIsNone(process_path(graph, [1, 3]))

    def test_process_empty_path(self):
        """Тестирование пустого пути"""
        graph = [None, {}, {1: 1}]
        self.assertEqual(process_path(graph, [], start=2), 2)

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