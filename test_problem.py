import unittest
from problem import Problem


class TestAdd(unittest.TestCase):

    def setUp(self):
        self._problem = Problem()

    def test_combo(self):
        l = [4, 5, 10]
        t = 10
        result = self._problem.combinationSum(t, l)
        self.assertEqual(result, [[5, 5], [10]])

if __name__ == '__main__':
    unittest.main()