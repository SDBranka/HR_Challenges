import unittest
import sys
sys.path.append("../..")
from implementation import gradingStudents


class test_gradingStudents(unittest.TestCase):
    def testZero(self):
        grades = [75, 67, 40, 33]
        self.assertEqual(gradingStudents(grades), [75, 67, 40, 33])

    def testThree(self):
        grades = [84, 94, 21, 0, 18, 100,18, 62, 30, 61, 53, 0, 
                    43, 2, 29, 53, 61, 40, 14, 4, 29, 98, 37, 23, 
                    46, 9, 79, 62, 20, 38, 51, 99, 59, 47, 4, 86, 
                    61, 68, 17, 45, 6, 1, 95, 95]
        self.assertEqual(gradingStudents(grades), [85, 95, 21, 0, 18, 100, 18, 62, 30, 61, 
                                                    55, 0, 45, 2, 29, 55, 61, 40, 14, 4, 29, 
                                                    100, 37, 23, 46, 9, 80, 62, 20, 40, 51, 
                                                    100, 60, 47, 4, 86, 61, 70, 17, 45, 6, 1, 
                                                    95, 95]
                                                    )



if __name__ == '__main__':
    unittest.main()       