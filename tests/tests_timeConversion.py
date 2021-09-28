import io
import unittest
import unittest.mock
import sys
sys.path.append("..")
from warmup_challenges import timeConversion

class test_miniMaxSum0(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        timeConversion(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        s = "12:01:00AM"
        self.assert_stdout(s, "00:01:00")

    def testTwo(self):
        s = "12:01:00PM"
        self.assert_stdout(s, "12:01:00")

    def testThree(self):
        s = "02:01:00AM"
        self.assert_stdout(s, "02:01:00")

    def testFour(self):
        s = "10:01:00PM"
        self.assert_stdout(s, "22:01:00")





if __name__ == '__main__':
    unittest.main()       