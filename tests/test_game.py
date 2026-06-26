# This module defines automatic tests with pytest

# Test snake
# Add conditions for snake-can grow in length only in one direction
# Grows in length only by one and only when he eats food

# Test food
# For each food eaten snake grows by one
# Food is spawn only after previous food was eaten
# Food is spawn on the board anywhere, except the obstacles

# Test game logic
# When snake crashes into himself, end of the board or obstacles: game over
# Starts with snake size 1x1 and in the middle of the board

# Test snake moves 
# Snakes moves by one square for each time step
# Snakes moves in the direction which was last typed by user
# Snake moves only byt the arrow keys

# Obstacles
# New obstacles are generated at new level
# Obstacles do not suddenly disappears
# Food is not spawned in an obstacle
# Snake is not spawned in an obstacle

import unittest
import numpy as np
import readchar
from snake.game_logic import spawn_food, snake_move, update_snake_position, end_game, execute_game_logic
from snake.levels import addVerticalBar, addBox, generate_levels


class TestSnakeGameLogic(unittest.TestCase):

    def setUp(self):
        # Initializes a standardized test board space before each testing cycle
        self.mock_board = np.zeros((20, 20), dtype=int)
        self.mock_edges = {(x, 0) for x in range(20)} | {(0, y) for y in range(20)}

    def test_snake_movement_directions(self):
        # Verifies that directional key inputs converts properly
        # Mock class to mimic readchar key behavior
        class MockKeys:
            LEFT = "left"
            RIGHT = "right"
            UP = "up"
            DOWN = "down"
            
        import readchar
        # Test moving right from center
        initial_snake = [(10, 10)]
        new_head = snake_move(initial_snake, readchar.key.RIGHT)
        self.assertEqual(new_head, (10, 11), "Snake failed to increment column moving right.")
        
        # Test moving up
        new_head = snake_move(initial_snake, readchar.key.UP)
        self.assertEqual(new_head, (9, 10), "Snake failed to decrement row moving up.")

    def test_snake_array_shifting(self):
        # Ensures the head insertion and tail popping functions preserve body
        current_body = [(10, 10), (10, 9), (10, 8)]
        next_head_coords = (10, 11)
        
        updated_body = update_snake_position(current_body, next_head_coords)
        
        self.assertEqual(updated_body[0], (10, 11), "New head position was not injected at index 0.")
        self.assertEqual(updated_body[1], (10, 10), "Body segments failed to shift downwards.")
        self.assertEqual(len(updated_body), 3, "Snake altered total array length during normal movement.")

    def test_collision_triggers(self):
        # Verifies that snake crashing into itself triggers game over
        # Test hitting outer borders
        dead_border_hit = end_game(False, self.mock_edges, (0, 5), [(0, 5)], [])
        self.assertTrue(dead_border_hit, "Game failed to catch outer border crash event.")
        
        # Test self-cannibalization crash
        snake_body = [(10, 10), (10, 9), (11, 9), (11, 10), (10, 10)]
        dead_self_hit = end_game(False, self.mock_edges, (10, 10), snake_body, [])
        self.assertTrue(dead_self_hit, "Game failed to catch snake biting its own body segments.")
        
        # Test crashing directly into obstacles
        active_obstacles = [(5, 5), (5, 6)]
        dead_obstacle_hit = end_game(False, self.mock_edges, (5, 5), [(5, 5)], active_obstacles)
        self.assertTrue(dead_obstacle_hit, "Game failed to intercept obstacle element crash.")

    def test_gate_placement_safety(self):
        #Guarantees portals never spawn dropped directly inside active grid obstacles
        static_obstacles = [(r, c) for r in range(1, 18) for c in range(1, 18)]
        generated_gate = spawn_food(self.mock_board, static_obstacles)
        
        self.assertNotIn(generated_gate, static_obstacles, "Gate generator spawned directly inside an obstacle block.")
        self.assertTrue(0 < generated_gate[0] < 19, "Gate coordinate row values escaped outer frame lines.")

    def test_shape_generators_flatness(self):
        # Ensures block vector tools return flat lists of tuples, not nested matrix layers
        vertical_bar = addVerticalBar(5, x=4, y=2)
        self.assertIsInstance(vertical_bar, list)
        self.assertEqual(len(vertical_bar), 5)
        self.assertIsInstance(vertical_bar[0], tuple)
        
        box_wall = addBox(3, x=5, y=5)
        # A 3x3 box should expand out to exactly 9 coordinate tuples
        self.assertEqual(len(box_wall), 9, "Box generation tool failed to assemble flat segment arrays.")

    def test_level_wiping_transitions(self):
        # Verifies level routing states overwrite old arrays on advancement ticks
        fresh_obstacles = generate_levels(level_tracker=0, obstacles=[], mode='Regular')
        self.assertEqual(fresh_obstacles, [], "Level 0 failed to wipe initial layouts clear.")
        
        level_one_obstacles = generate_levels(level_tracker=1, obstacles=[], mode='Random')
        self.assertTrue(len(level_one_obstacles) > 0, "Level router failed to populate level 1 blocks.")
    
    def test_snake_growth_on_food(self):
        # Verifies that a new segment is inserted at the end of snake list after eating food
        snake_body = [(10, 10), (10, 9), (10, 8), (10, 7), (10, 6)]
        food = (10, 10)
        
        updated_snake_body = execute_game_logic((10, 10), snake_body, food, 1, readchar.key.RIGHT, [], 0, [], False, 'Classic')
        
        self.assertTrue((len(updated_snake_body) - len(snake_body)) == 1, "Game logic failed to growth snake after eating food.")


if __name__ == '__main__':
    unittest.main()