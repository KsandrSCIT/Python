import unittest
import lab1

class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = lab1.summ_two_numbers(9, [2,7,11,15])
        self.assertEqual(result,[0,1], "exampl 1")
    def test_something2(self):
        result = lab1.summ_two_numbers(6, [3,2,4])
        self.assertEqual(result, [1,2], "exampl 2")
    def test_something3(self):
        result = lab1.summ_two_numbers(6, [3,3])
        self.assertEqual(result, [0,1], "exampl 3")
