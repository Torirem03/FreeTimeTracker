"""
* Name : FreeTime Tracker Map class tests
* Author: Amber Miller
* Created : 12/5/2023
* Course: CIS 152 - Data Structure
* Version: 1.0
* OS: MAC OS Ventura 13.5.1
* IDE: PyCharm 2023.2.1 (Professional Edition) Version
* Copyright : This is my own original work
* based on specifications issued by our instructor
* Description : Unit testing for Map data structure in FreeTime Tracker project
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified. I have not given other fellow student(s) access
* to my program.
"""
from unittest import TestCase
import gameMap


class TestMap(TestCase):
    games = gameMap.Map()
    games.insert_pair("WoW", 1)
    games.insert_pair("Super Mario RPG", 2)
    games.insert_pair("Chrono Trigger", 4)

    def test_valid_key_True(self):
        self.assertEqual(self.games.valid_key("Chrono Trigger"), True)

    def test_valid_key_False(self):
        self.assertEqual(self.games.valid_key("Bugsnax"), False)

    def test_find_value_found(self):
        self.assertEqual(self.games.find_value("WoW"), 1)

    def test_find_value_NOT_found(self):
        self.assertEqual(self.games.find_value("MegaMan"), "Key not found!")

    def test_insert_pair_True(self):
        self.assertEqual(self.games.insert_pair("Overwatch 2", 3), True)

    def test_insert_pair_False(self):
        self.assertEqual(self.games.insert_pair("Super Mario RPG", 3), False)

    def test_remove_pair_True(self):
        self.assertEqual(self.games.remove_pair("WoW"), True)

    def test_remove_pair_False(self):
        self.assertEqual(self.games.remove_pair("Bugsnax"), False)

    def test_print_map(self):
        mappy = self.games.map
        self.assertEqual(self.games.print_map(), mappy)
