import unittest
import os
import sys

# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)
import Processing

#creating a object for class Process
obj_process = Processing.Process()

class TestAllCases(unittest.TestCase):
    def test_MOVE_IN(self):
        # creating a object for class Process
        obj_process = Processing.Process()

        input_line_1 = "MOVE_IN ANDY"
        expected_result = True
        actual_result = obj_process.MOVE_IN(input_line_1)
        self.assertEqual(expected_result,actual_result)

        #adding 2nd member
        input_line_2 = "MOVE_IN WOODY"
        obj_process.MOVE_IN(input_line_2)

        #adding 3rd member
        input_line_3 = "MOVE_IN BO"
        obj_process.MOVE_IN(input_line_3)

        # adding 4th member when already 3 members are filled
        input_line_4 = "MOVE_IN REX"
        expected_result = False
        actual_result = obj_process.MOVE_IN(input_line_4)
        self.assertEqual(expected_result, actual_result)

    def test_SPEND(self):
        # creating a object for class Process
        obj_process = Processing.Process()

        # first need to MOVE_IN members
        pre_input_line_1 = "MOVE_IN ANDY"
        obj_process.MOVE_IN(pre_input_line_1)
        pre_input_line_2 = "MOVE_IN WOODY"
        obj_process.MOVE_IN(pre_input_line_2)
        pre_input_line_3 = "MOVE_IN BO"
        obj_process.MOVE_IN(pre_input_line_3)

        # adding SPEND after MOVE_IN
        input_line_1 = "SPEND 3000 ANDY WOODY BO"
        expected_result = True
        actual_result = obj_process.SPEND(input_line_1)
        self.assertEqual(expected_result,actual_result)

        #adding 2nd SPEND
        input_line_2 = "SPEND 300 WOODY BO"
        obj_process.SPEND(input_line_2)

        #adding 3rd SPEND
        input_line_3 = "SPEND 300 WOODY REX"
        expected_result = False
        actual_result = obj_process.SPEND(input_line_3)
        self.assertEqual(expected_result, actual_result)

    def test_DUES(self):
        # creating a object for class Process
        obj_process = Processing.Process()

        # first need to MOVE_IN members
        pre_input_line_1 = "MOVE_IN ANDY"
        obj_process.MOVE_IN(pre_input_line_1)
        pre_input_line_2 = "MOVE_IN WOODY"
        obj_process.MOVE_IN(pre_input_line_2)
        pre_input_line_3 = "MOVE_IN BO"
        obj_process.MOVE_IN(pre_input_line_3)

        # second need to add SPEND after MOVE_IN
        pre_input_line_4 = "SPEND 3000 ANDY WOODY BO"
        obj_process.SPEND(pre_input_line_4)
        pre_input_line_5 = "SPEND 300 WOODY BO"
        obj_process.SPEND(pre_input_line_5)
        pre_input_line_6 = "SPEND 300 WOODY REX"
        obj_process.SPEND(pre_input_line_6)

        # Dues comes after spend
        input_line_1 = "DUES BO"
        expected_result = True
        actual_result = obj_process.DUES(input_line_1)
        self.assertEqual(expected_result,actual_result)

        #retreiving 2nd member DUE
        input_line_2 = "DUES WOODY"
        expected_result = True
        actual_result = obj_process.DUES(input_line_2)
        self.assertEqual(expected_result, actual_result)

        #retreiving 3rd member DUES
        input_line_3 = "DUES REX"
        expected_result = False
        actual_result = obj_process.DUES(input_line_3)
        self.assertEqual(expected_result, actual_result)