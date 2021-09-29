import io
import unittest
import unittest.mock
import sys
sys.path.append("..")
from implementation import countApplesAndOranges

class test_countApplesAndOranges(unittest.TestCase):

    # @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    # def assert_stdout(self, n, expected_output, mock_stdout):
    #     countApplesAndOranges(n)
    #     self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, s, t, a, b, apples, oranges, expected_output, mock_stdout):
        countApplesAndOranges(s, t, a, b, apples, oranges)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testZero(self):
        s = 7 
        t = 11
        a = 5 
        b = 15
        m = 3 
        n = 2
        apples = [-2, 2, 1]
        oranges = [5, -6]
        self.assert_stdout(s, t, a, b, apples, oranges, "1\n1")

    def testOne(self):
        s = 7
        t = 10
        a = 4
        b = 12
        m = 3
        n = 3 
        apples = [2, 3, -4] 
        oranges = [3, -2, -4] 
        self.assert_stdout(s, t, a, b, apples, oranges, "1\n2")



# countApplesAndOranges(s, t, a, b, apples, oranges)



if __name__ == '__main__':
    unittest.main()       