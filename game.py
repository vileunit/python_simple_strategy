"""
A simple Python strategy game
"""

import numpy as np

WALKABLE = 0
CHARACTER = 1
WALL = 2
HIDDEN = 9


# Transform a row and column count into a Level
# generate_level :: Int -> Int -> Level
def generate_level():
    return np.array(
        [[0, 0, 0, 0, 0],
         [2, 2, 2, 2, 0],
         [2, 2, 2, 0, 0],
         [2, 2, 2, 0, 2],
         [0, 1, 0, 0, 0]]
    )


# Get the index of the character location from the level
# get_current_position :: Level -> Int -> [(Int, Int)]
def get_current_position(level, character):
    return np.asarray(
        np.where(
            level == character
        )
    )


'''
Test Function
'''
print(
    get_current_position(
        generate_level(),
        CHARACTER
    )
)
