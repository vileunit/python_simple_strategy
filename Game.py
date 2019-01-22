"""
A simple Python strategy game
"""

import numpy as np

# Tile Settings
WALKABLE = 0
CHARACTER = 1
WALL = 2
HIDDEN = 9

# Level Settings
LEVEL_HEIGHT = 5
LEVEL_WIDTH = 5
VISION_LENGTH = 1

'''
Level Functions
'''


# Transform a row and column count into a Level
# generate_level :: Int -> Int -> Level
def generate_level(height, width):
    level = np.array(
        [[0, 0, 0, 0, 0],
         [2, 2, 2, 2, 0],
         [2, 2, 2, 0, 0],
         [2, 2, 2, 0, 2],
         [0, 1, 0, 0, 0]]
    )
    return level


# Get the index of the character location from the level
# get_current_position :: Level -> Int -> (Int, Int)
def get_current_position(level, character):
    pos = np.asarray(
        np.where(
            level == character
        )
    )
    return pos[0][0], pos[1][0]


# Make changes to the level state
# update_level :: Level -> Int -> Int -> Int -> Int -> Level
def update_level_movement(level, current_row, current_column, new_row, new_column):
    level[new_row][new_column] = 1
    level[current_row][current_column] = 0
    return level


# Limit the lower boundary of the level
# control_lower_boundary :: Int -> Int -> Int -> Int
def control_lower_boundary(axis_value, boundary, vision_length):
    space = axis_value - vision_length
    return boundary if space < boundary else space


# Limit the upper boundary of the level
# control_upper_boundary :: Int -> Int -> Int -> Int
def control_upper_boundary(axis_value, boundary, vision_length):
    space = axis_value + vision_length + 1
    return boundary if space > boundary else space


# Hide parts of the level not visible by character
# toggle_fog :: Level -> Int -> Level
def toggle_fog(level, height, width, vision_length):
    fog = np.full_like(level, 9)
    tile_row, tile_column = get_current_position(level, CHARACTER)
    top = control_lower_boundary(tile_row, 0, vision_length)
    left = control_lower_boundary(tile_column, 0, vision_length)
    bottom = control_upper_boundary(tile_row, height, vision_length)
    right = control_upper_boundary(tile_column, width, vision_length)
    fog[top:bottom, left:right] = level[top:bottom, left:right]
    return fog


'''
Action Functions
'''


# Transition state based on action performed
# perform_action :: Level -> Action -> Level
def perform_action(level, action):
    if action == "up":
        return move_up(level, CHARACTER, WALKABLE)
    if action == "down":
        return move_down(level, CHARACTER, WALKABLE)
    if action == "left":
        return move_left(level, CHARACTER, WALKABLE)
    if action == "right":
        return move_right(level, CHARACTER, WALKABLE)

    return level


# Transition state based on up action performed
# move_up :: Level -> Level
def move_up(level, character_tile, walkable_tile):
    tile_row, tile_column = get_current_position(level, character_tile)

    if (tile_row != 0) and (level[tile_row - 1][tile_column] == walkable_tile):
        return update_level_movement(level, tile_row, tile_column, tile_row - 1, tile_column)

    return level


# Transition state based on down action performed
# move_down :: Level -> Level
def move_down(level, character_tile, walkable_tile):
    tile_row, tile_column = get_current_position(level, character_tile)

    if (tile_row != 4) and (level[tile_row + 1][tile_column] == walkable_tile):
        return update_level_movement(level, tile_row, tile_column, tile_row + 1, tile_column)

    return level


# Transition state based on left action performed
# move_left :: Level -> Level
def move_left(level, character_tile, walkable_tile):
    tile_row, tile_column = get_current_position(level, character_tile)

    if (tile_column != 0) and (level[tile_row][tile_column - 1] == walkable_tile):
        return update_level_movement(level, tile_row, tile_column, tile_row, tile_column - 1)

    return level


# Transition state based on right action performed
# move_right :: Level -> Level
def move_right(level, character_tile, walkable_tile):
    tile_row, tile_column = get_current_position(level, character_tile)

    if (tile_column != 4) and (level[tile_row][tile_column + 1] == walkable_tile):
        return update_level_movement(level, tile_row, tile_column, tile_row, tile_column + 1)

    return level


'''
Test Functions
'''


def test_navigate_level_success():
    foo = generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
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


def test_display_fog_success():
    foo = generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
    print(toggle_fog(foo, LEVEL_HEIGHT, LEVEL_WIDTH, VISION_LENGTH))
