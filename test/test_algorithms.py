import unittest
from search import algorithms
from search import data_generator
from search import constants

arrays =  [
    [3],
    [1, 7],
    [2, 5, 8],
    [4, 9, 12],
    [6, 11, 15, 19],
    [10, 14, 18, 22],
    [5, 13, 17, 21],
    [8, 16, 24, 32, 40],
    [12, 20, 28, 36, 44],
    [11, 23, 35, 47, 59, 71],
    [9, 18, 27, 36, 45, 54],
    [13, 26, 39, 52, 65, 78],
    [17, 34, 51, 68, 85, 102, 119],
    [19, 38, 57, 76, 95, 114, 133],
    [14, 28, 42, 56, 70, 84, 98, 112],
    [16, 32, 48, 64, 80, 96, 112, 128],
    [20, 40, 60, 80, 100, 120, 140, 160],
    [18, 36, 54, 72, 90, 108, 126, 144, 162],
    [22, 44, 66, 88, 110, 132, 154, 176, 198, 220],
    [15, 30, 45, 60, 75, 90, 105, 120, 135, 150]
]

values = [3, 4, 8, 9, 20, 22, 13, 32, 28, 59, 36, 39, 68, 95, 56, 96, 120, 126, 100, 90]
expected = [0, -1, 2, 1, -1, 3, 1, 3, 2, 4, 3, 2, 3, 4, 3, 5, 5, 6, -1, 5]


class AlgorithmsTests(unittest.TestCase):
    def test_linear_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.linearSearch(array, values[i])
            self.assertEqual(result, expected[i])

    def test_binary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.binarySearch(array, values[i])
            self.assertEqual(result, expected[i])

    def test_ternary_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.ternarySearch(array, values[i])
            self.assertEqual(result, expected[i])

    def test_jump_search(self):
        for i in range(len(arrays)):
            array = arrays[i]
            result = algorithms.jumpSearch(array, values[i])
            self.assertEqual(result, expected[i])

if __name__ == "__main__":
    unittest.main()
