import unittest

from algoritma import insertionsort

class testInsertionSort(unittest.TestCase):
    def test_list_int(self):
        data = [3,6,4,7,9,2]
        result = insertionsort(list)
        self.assertEqual(result, 3,6,4,7,9,2)

if __name__ == "__main__":
    unittest.main()