"""
Dice class for the battle simulator
This class represents a dice with a specified number of sides. It can be rolled to produce a random integer between 1 and the number of sides.
The dice can also be called as a function to roll it, and it has a string representation for easy debugging and display.
The Dice class is used in conjunction with the Weapon class to determine the damage dealt by weapons in the battle simulator.
"""

# Task 2: Dice class

import random

class Dice:

    def __init__(self, sides: int = 6) -> None:
        '''
        Initialises the Dice

        Args:
            sides(int): number of sides om the dice, default = 6
        '''
        if sides < 2:
            raise ValueError('Number of sides must be 2 or more')
        self.sides = sides

    def roll(self) -> int:
        '''Returns a random number between 1 and the number of sides'''
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        '''Representation of Dice object'''
        return f'Dice(sides={self.sides})'

    def __call__(self):
        '''Rolls the dice when the object is called as a function'''
        return self.roll()
