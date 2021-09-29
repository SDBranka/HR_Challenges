import io
import unittest
import unittest.mock
import sys
sys.path.append("../..")
from warmup_challenges import plusMinus


class test_simpleArraySum(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        plusMinus(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 1, 0, -1, -1]
        self.assert_stdout(arr, "0.400000\n0.400000\n0.200000\n")

    def testTwo(self):
        arr = [-4, 3, -9, 0, 4, 1]
        self.assertEqual(arr, "0.500000\n0.333333\n0.166667\n")

    def testThree(self):
        ar = [1, 2, 3, -1, -2, -3, 0, 0]
        self.assertEqual(arr, "0.375000\n0.375000\n0.250000")



if __name__ == '__main__':
    unittest.main()       