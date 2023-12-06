"""
* Name : FreeTime Tracker Map class
* Author: Amber Miller
* Created : 12/5/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: MAC OS Ventura 13.5.1
* IDE: PyCharm 2023.2.1 (Professional Edition) Version
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : Map data structure class used in FreeTime Tracker project
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""


class Map:
    # constructor that also initializes/creates an empty dictionary for the class
    def __init__(self):
        self.map = {}

    # Method that checks to see if key is already in dictionary, returns true if it is, false if it is not
    def valid_key(self, key):
        if key in self.map.keys():
            return True
        else:
            return False

    # Method that finds the corresponding value to the parameter key
    def find_value(self, key):
        # if key is in the dictionary, it returns the value to that key
        if self.valid_key(key):
            return self.map.get(key)
        # else, it returns an error message to the user
        else:
            return "Key not found!"

    # Method that inserts a key/value pair into the dictionary
    def insert_pair(self, new_key, new_value):
        # if key already exists in the dictionary, false returns as keys must be unique
        if self.valid_key(new_key):
            return False
        # else, we add the new key/value pair to the dictionary
        else:
            self.map[new_key] = new_value
            return True

    # Method that removes a key/value pair from the dictionary
    def remove_pair(self, old_key):
        # if key exists in the dictionary, key and associated value are removed from the dictionary
        if self.valid_key(old_key):
            del self.map[old_key]
            return True
        # if key doesn't exist in dictionary, false returns
        else:
            return False

    # Method that prints the dictionary/map
    def print_map(self):
        return self.map
