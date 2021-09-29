import io
import unittest
import unittest.mock
import sys
sys.path.append("../..")
from warmup_challenges import miniMaxSum0, miniMaxSum1


class test_miniMaxSum0(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        miniMaxSum0(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 2, 3, 4, 5]
        self.assert_stdout(arr, "10 14")


class test_miniMaxSum1(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        miniMaxSum1(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        arr = [1, 2, 3, 4, 5]
        self.assert_stdout(arr, "10 14")



if __name__ == '__main__':
    unittest.main()       