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
    level = np.array(
        [[0, 0, 0, 0, 0],
         [2, 2, 2, 2, 0],
         [2, 2, 2, 0, 0],
         [2, 2, 2, 0, 2],
         [0, 1, 0, 0, 0]]
    )
    print("New level")
    print(level)
    print("\n")
    return level


# Make changes to the level state
# update_level :: Level -> Int -> Int -> Int -> Int -> Level
def update_level(level, current_row, current_column, new_row, new_column):
    level[new_row][new_column] = 1
    level[current_row][current_column] = 0
    return level


# Get the index of the character location from the level
# get_current_position :: Level -> Int -> [[Int][Int]]
def get_current_position(level, character):
    return np.asarray(
        np.where(
            level == character
        )
    )


# Transition state based on action performed
# perform_action :: Level -> Action -> Level
def perform_action(level, action):
    if action == "up":
        return move_up(level)
    if action == "down":
        return move_down(level)
    if action == "left":
        return move_left(level)
    if action == "right":
        return move_right(level)

    return level


# Transition state based on up action performed
# move_up :: Level -> Level
def move_up(level):
    pos = get_current_position(level, CHARACTER)
    row_tile = pos[0][0]
    column_tile = pos[1][0]
    if (row_tile != 0) and (level[row_tile - 1][column_tile] == WALKABLE):
        print(level)
        print("\n")
        print("Moving up")
        return update_level(level, row_tile, column_tile, row_tile - 1, column_tile)

    print(level)
    print("\n")
    print("Moving up")
    return level


# Transition state based on down action performed
# move_down :: Level -> Level
def move_down(level):
    pos = get_current_position(level, CHARACTER)
    row_tile = pos[0][0]
    column_tile = pos[1][0]
    if (row_tile != 4) and (level[row_tile + 1][column_tile] == WALKABLE):
        print(level)
        print("\n")
        print("Moving down")
        return update_level(level, row_tile, column_tile, row_tile + 1, column_tile)

    print(level)
    print("\n")
    print("Moving down")
    return level


# Transition state based on left action performed
# move_left :: Level -> Level
def move_left(level):
    pos = get_current_position(level, CHARACTER)
    row_tile = pos[0][0]
    column_tile = pos[1][0]
    if (column_tile != 0) and (level[row_tile][column_tile - 1] == WALKABLE):
        print(level)
        print("\n")
        print("Moving left")
        return update_level(level, row_tile, column_tile, row_tile, column_tile - 1)

    print(level)
    print("\n")
    print("Moving left")
    return level


# Transition state based on right action performed
# move_right :: Level -> Level
def move_right(level):
    pos = get_current_position(level, CHARACTER)
    row_tile = pos[0][0]
    column_tile = pos[1][0]
    if (column_tile != 4) and (level[row_tile][column_tile + 1] == WALKABLE):
        print(level)
        print("\n")
        print("Moving right")
        return update_level(level, row_tile, column_tile, row_tile, column_tile + 1)

    print(level)
    print("\n")
    print("Moving right")
    return level


'''
Test Function
'''
foo = generate_level()
foo = perform_action(foo, "up")
foo = perform_action(foo, "left")
foo = perform_action(foo, "down")
foo = perform_action(foo, "right")
foo = perform_action(foo, "right")
foo = perform_action(foo, "right")
foo = perform_action(foo, "up")
foo = perform_action(foo, "up")
foo = perform_action(foo, "right")
foo = perform_action(foo, "up")
foo = perform_action(foo, "up")
foo = perform_action(foo, "left")
foo = perform_action(foo, "left")
foo = perform_action(foo, "left")
foo = perform_action(foo, "left")
print(foo)
