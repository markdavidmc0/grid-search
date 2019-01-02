#!/usr/bin/env python

import unittest
from search import GridSearch


class TestSearch(unittest.TestCase):
    """Test script for shortest path finding for grid objective"""

    GRID1 = [
                [1, 0, 0, 0, 1, 0],
                [1, 1, 1, 0, 1, 0],
                [1, 0, 1, 0, 1, 0],
                [1, 1, 1, 0, 1, 0],
                [1, 1, 1, 9, 1, 0],
                [1, 0, 0, 0, 1, 9]
        ]

    def test_case_basic(self):
        grid_1 = TestSearch.GRID1
        n = 6
        output = GridSearch(n, grid_1).search()
        print(output)


if __name__ == '__main__':
    unittest.main()
