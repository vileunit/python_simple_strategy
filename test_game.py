from unittest import TestCase
import numpy as np

import Game

# Tile Settings
WALKABLE = 0
CHARACTER = 1
WALL = 2
HIDDEN = 9

# Level Settings
CHARACTER_COUNT = 1
LEVEL_HEIGHT = 5
LEVEL_WIDTH = 5
VISION_LENGTH = 1


class TestGame(TestCase):
    def test_generate_level(self):
        level = Game.generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
        (x, y) = level.shape
        character_count = level[np.where(level == 1)]

        self.assertEqual(x, LEVEL_HEIGHT)
        self.assertEqual(y, LEVEL_WIDTH)
        self.assertEqual(character_count.size, CHARACTER_COUNT)

    def test_get_current_position(self):
        level = Game.generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
        (start_x, start_y) = Game.get_current_position(level, CHARACTER)

        self.assertEqual(level[start_x][start_y], 1)

    def test_update_level(self):
        level = Game.generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
        (start_x, start_y) = Game.get_current_position(level, CHARACTER)
        (end_x, end_y) = (4, 3)
        result_level = Game.update_level_movement(level, start_x, start_y, end_x, end_y)

        self.assertEqual(result_level[start_x][start_y], 0)
        self.assertEqual(result_level[end_x][end_y], 1)

    def test_control_lower_boundary(self):
        self.assertEqual(Game.control_lower_boundary(2, 0, 3), 0)
        self.assertEqual(Game.control_lower_boundary(2, 0, 2), 0)
        self.assertEqual(Game.control_lower_boundary(2, 0, 1), 1)

    def test_control_upper_boundary(self):
        self.assertEqual(Game.control_upper_boundary(2, 4, 3), 4)
        self.assertEqual(Game.control_upper_boundary(2, 4, 2), 4)
        self.assertEqual(Game.control_upper_boundary(2, 4, 1), 4)

    def test_toggle_fog_with_vision_1(self):
        level = Game.generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
        fog_level = np.array(
            [[9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [2, 2, 2, 9, 9],
             [0, 1, 0, 9, 9]]
        )
        result_level = Game.toggle_fog(level, LEVEL_HEIGHT, LEVEL_WIDTH, 1)
        self.assertTrue(np.array_equal(fog_level, result_level))

    def test_toggle_fog_with_vision_2(self):
        level = Game.generate_level(LEVEL_HEIGHT, LEVEL_WIDTH)
        fog_level = np.array(
            [[9, 9, 9, 9, 9],
             [9, 9, 9, 9, 9],
             [2, 2, 2, 0, 9],
             [2, 2, 2, 0, 9],
             [0, 1, 0, 0, 9]]
        )
        result_level = Game.toggle_fog(level, LEVEL_HEIGHT, LEVEL_WIDTH, 2)
        self.assertTrue(np.array_equal(fog_level, result_level))

        #
        # def test_perform_action(self):
        #     self.fail()
        #
        # def test_move_up(self):
        #     self.fail()
        #
        # def test_move_down(self):
        #     self.fail()
        #
        # def test_move_left(self):
        #     self.fail()
        #
        # def test_move_right(self):
        #     self.fail()
