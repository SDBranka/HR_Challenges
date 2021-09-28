import io
import unittest
import unittest.mock
import sys
sys.path.append("..")
from warmup_challenges import staircase

class test_staircase(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        staircase(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def testOne(self):
        n = 6
        self.assert_stdout(n, "     #\n    ##\n   ###\n  ####\n #####\n######\n")



if __name__ == '__main__':
    unittest.main()       