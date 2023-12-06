"""
* Name : FreeTime Tracker Stack Queue class tests
* Author: Amber Miller
* Created : 12/5/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: MAC OS Ventura 13.5.1
* IDE: PyCharm 2023.2.1 (Professional Edition) Version
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : Unit testing for Stack data structure in FreeTime Tracker project
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""

from unittest import TestCase
import crochetSQ


class TestStack(TestCase):
    crochet = crochetSQ.Stack()
    crochet.push("Octopus Hat")
    crochet.push("Glamrock Freddy")
    crochet.push("Boomer amigurumi")

    def test_is_empty_False(self):
        self.assertEqual(self.crochet.is_empty(), False)

    def test_is_empty_True(self):
        newStack = crochetSQ.Stack()
        self.assertEqual(newStack.is_empty(), True)

    def test_push_and_peek(self):
        new_item = "Candy Cane ornament"
        self.crochet.push(new_item)
        top_stack = self.crochet.peek()
        self.assertEqual(top_stack, new_item)

    def test_size(self):
        expected_size = 4
        self.assertEqual(self.crochet.size(), expected_size)

    def test_print_stack_up(self):
        crochet_list = self.crochet.items
        self.assertEqual(self.crochet.print_stack_up(), crochet_list)
