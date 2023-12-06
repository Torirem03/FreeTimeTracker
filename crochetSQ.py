"""
* Name : FreeTime Tracker Stack class
* Author: Amber Miller
* Created : 12/5/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: MAC OS Ventura 13.5.1
* IDE: PyCharm 2023.2.1 (Professional Edition) Version
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : Stack data structure class used in FreeTime Tracker project
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


class Stack:
    # constructor that also initializes/creates an empty list for the class and sets size to 0
    def __init__(self):
        self.items = []
        self.list_size = 0

    # method that checks if the stack is currently void of items
    def is_empty(self):
        if self.list_size == 0:
            return True
        else:
            return False

    # method that will add an item to the end/top of the stack and increase the size counter of the list
    def push(self, item):
        self.items.append(item)
        self.list_size += 1

    # method that will remove the last item in the stack if the list isn't empty
    def pop(self):
        if self.is_empty():
            raise Exception("Stack empty")

        self.items.pop(-1)
        self.list_size -= 1

    # method that shows the user what item is on top of the stack without altering the stack
    def peek(self):
        if self.is_empty():
            raise Exception("Stack empty")
        return self.items[-1]

    # method that returns the size/length of the list
    def size(self):
        return self.list_size

    # method that will print the stack list
    def print_stack_up(self):
        return self.items

