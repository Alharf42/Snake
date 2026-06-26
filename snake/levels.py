# Obstacles - list of tuples
# Track level number
# gate
# obstacles must be outside of boarder edges
# food must be generated outside of obstacles
# snake going into an obstacle dies
# new level rewrites previous obstacles

import random

obstacles = []


def spawn_gate(board, obstacles):
    inObstacle = True
    gate = (0, 0)
    while inObstacle:
        gate = (random.randint(0+1, len(board)-1-1), random.randint(0+1, len(board)-1-1))
        if gate not in obstacles:
            inObstacle = False
    return gate


def inFreeSpace(list, obstacles):
    if (10, 10) not in list and list not in obstacles:
        return True


def addVerticalBar(length, x, y):
    newObstacle = [(x, k) for k in range(y, y+length)]
    return newObstacle


def addHorizontalBar(length, x, y):
    newObstacle = [(k, y) for k in range(x, x+length)]
    return newObstacle


def addBox(length, x, y):
    newObstacle = []
    temp = length
    while temp != 0:
        newObstacle.extend(addVerticalBar(length, x, y))
        x = x+1
        temp = temp-1
    return newObstacle


def addL(length, x, y):
    newObstacle = []
    newObstacle.extend(addVerticalBar(length-1, x, y))
    newObstacle.extend(addHorizontalBar(length-1, x, y))
    return newObstacle


def addReverseL(length, x, y):
    newObstacle = []
    newObstacle.extend(addVerticalBar(length-1, x, y))
    newObstacle.extend(addHorizontalBar(length-1, y, x))
    return newObstacle


# Functions that creates a random level
# Random level constitutes of shapes created from functions above.
# Their variety, length and coordinates are assigned randomly.
# It goes with the risk of some random levels being unplayable, due to
# existing fully enclosed ares the snake is incapable of entering or leaving.
def random_level(obstacles):
    numObstacles = random.randint(2, 8)
    newObstacles = []
    inStart = True
    while (numObstacles):
        length = 0
        x = 0
        y = 0
        obstacle = []
        whichObstacle = random.randint(1, 5)
        while (inStart):
            length = random.randint(3, 15)
            x = random.randint(1, 19)
            y = random.randint(1, 19)
            match whichObstacle:
                case 1:
                    obstacle = addVerticalBar(length, x, y) 
                case 2:
                    obstacle = addHorizontalBar(length, x, y)
                case 3:
                    obstacle = addL(length, x, y)
                case 4: 
                    obstacle = addBox(length, x, y)
                case 5:
                    obstacle = addReverseL(length, x, y)
            if (10, 10) not in obstacle:
                inStart = False
        newObstacles.extend(obstacle)
        inStart = True
        numObstacles -= 1
    obstacles = newObstacles
    return obstacles


# This function is used to assign a specific set of obstacles for each level
def generate_levels(level_tracker, obstacles, mode):
    if obstacles:
        return obstacles
    
    if mode == 'Regular' or mode == 'Classic':
        match level_tracker:
            case 0:
                obstacles = []
            case 1:
                obstacles = addVerticalBar(8, 6, 6)
                obstacles.extend(addVerticalBar(8, 14, 6))
            case 2:
                obstacles = addHorizontalBar(8, 6, 6)
                obstacles.extend(addHorizontalBar(8, 6, 14))
            case 3:
                obstacles = addL(5, 5, 5)
                obstacles.extend(addReverseL(5, 15, 12))
            case 4:
                # Four crosses
                # Top left (centered at X=5, Y=5)
                obstacles = addHorizontalBar(5, 3, 5)  # Left-to-right
                obstacles.extend(addVerticalBar(5, 5, 3))  # Top-to-bottom
                # Top right (centered at X=14, Y=5)
                obstacles.extend(addHorizontalBar(5, 12, 5))
                obstacles.extend(addVerticalBar(5, 14, 3))
                # bottom left (centered at X=5, Y=14)
                obstacles.extend(addHorizontalBar(5, 3, 14))
                obstacles.extend(addVerticalBar(5, 5, 12))
                # bottom right (centered at X=14, Y=14)
                obstacles.extend(addHorizontalBar(5, 12, 14))
                obstacles.extend(addVerticalBar(5, 14, 12))
            case 5:
                # A long upper bar with a 3-block safety window on 
                # the left/right edges
                obstacles = addHorizontalBar(14, 3, 6)
                
                # A long lower bar matching the top
                obstacles.extend(addHorizontalBar(14, 3, 13))

                # Small vertical bars that break up the middle)
                obstacles.extend(addVerticalBar(2, 7, 9))
                obstacles.extend(addVerticalBar(2, 13, 9))
            case 6:
                # Upper funnel ceiling dropping down
                obstacles = addVerticalBar(4, 6, 2)
                obstacles.extend(addVerticalBar(4, 14, 2))
                obstacles.extend(addHorizontalBar(9, 6, 5))
                
                # Lower funnel floor reaching up
                obstacles.extend(addVerticalBar(4, 6, 14))
                obstacles.extend(addVerticalBar(4, 14, 14))
                obstacles.extend(addHorizontalBar(9, 6, 14))

                # Extra center teeth to enforce the narrow corridor
                obstacles.extend([(9, 7), (9, 12)])
            case 7:
                # Four boxes
                # Top left
                obstacles = addBox(4, 3, 3)
                # Bottom right
                obstacles.extend(addBox(4, 13, 13))
                # Bottom left
                obstacles.extend(addBox(4, 3, 13))
                # Top right
                obstacles.extend(addBox(4, 13, 3))
            case 8:
                # 6 crosses
                # top row (y = 4)
                # Top left cross (centered at x=4, y=4)
                obstacles = addHorizontalBar(3, 3, 4)
                obstacles.extend(addVerticalBar(3, 4, 3))
                # Top center cross (centered at x=10, y=4)
                obstacles.extend(addHorizontalBar(3, 9, 4))
                obstacles.extend(addVerticalBar(3, 10, 3))
                # Top right cross (centered at x=16, y=4)
                obstacles.extend(addHorizontalBar(3, 15, 4))
                obstacles.extend(addVerticalBar(3, 16, 3))
                # Bottom row (y = 15)
                # Bottom left cross (centered at x=4, y=15)
                obstacles.extend(addHorizontalBar(3, 3, 15))
                obstacles.extend(addVerticalBar(3, 4, 14))
                # Bottom center (centered at x=10, y=15)
                obstacles.extend(addHorizontalBar(3, 9, 15))
                obstacles.extend(addVerticalBar(3, 10, 14))
                # Bottom right (centered at x=16, y=15)
                obstacles.extend(addHorizontalBar(3, 15, 15))
                obstacles.extend(addVerticalBar(3, 16, 14))
            case 9:
                obstacles = []
                # Top wall bars
                for x in [4, 8, 12, 16]:
                    obstacles.extend(addVerticalBar(3, x, 2))
                    
                # Bottom wall bars
                for x in [4, 8, 12, 16]:
                    obstacles.extend(addVerticalBar(3, x, 15))
                    
                # Left/Right
                obstacles.extend(addVerticalBar(6, 3, 7))
                obstacles.extend(addVerticalBar(6, 17, 7))
            case 10:
                # Top vertical divider (stops right before the center)
                obstacles = addVerticalBar(5, 10, 2)
                obstacles.extend(addVerticalBar(5, 9, 2))
                # Bottom vertical divider
                obstacles.extend(addVerticalBar(5, 10, 13))
                obstacles.extend(addVerticalBar(5, 9, 13))
                
                # Left horizontal divider
                obstacles.extend(addHorizontalBar(5, 2, 10))
                obstacles.extend(addHorizontalBar(5, 2, 9))
                # Right horizontal divider
                obstacles.extend(addHorizontalBar(5, 13, 10))
                obstacles.extend(addHorizontalBar(5, 13, 9))
                
                # Corner pocket
                obstacles.extend([(4, 4), (15, 4), (4, 15), (15, 15)])
            case 11:
                # Top left L
                for col in range(2, 15):
                    obstacles.append((2, col))  # Top bar
                for row in range(2, 14):
                    obstacles.append((row, 2))  # Left descending bar
                for col in range(2, 11):
                    obstacles.append((13, col))  # Bottom bar turning inward

                # Bottom right L
                for col in range(5, 18):
                    obstacles.append((17, col))  # Bottom bar
                for row in range(6, 18):
                    obstacles.append((row, 17))  # Right ascending bar
                for col in range(9, 18):
                    obstacles.append((6, col))  # Top bar turning inward
            case 12:
                # 2x2 corner pillar blocks
                corner_blocks = [
                    (4, 4), (4, 5), (5, 4), (5, 5),      # Top left
                    (4, 14), (4, 15), (5, 14), (5, 15),  # Top right
                    (14, 4), (14, 5), (15, 4), (15, 5),  # Bottom left
                    (14, 14), (14, 15), (15, 14), (15, 15) # Bottom right
                ]
                obstacles.extend(corner_blocks)

                # Left center
                obstacles.extend([(8, 6), (8, 7), (8, 8)])
                # Right center
                obstacles.extend([(11, 11), (11, 12), (11, 13)])
                # Center
                obstacles.extend([(7, 12), (12, 7)])
            case 13:
                # The Vault
                # Creates a hollow central square from index 6 to 14
                for i in range(6, 15):
                    # Draw lines but leave a single gap exactly at index 10 (the middle)
                    if i != 10:
                        obstacles.append((6, i))
                        obstacles.append((14, i))
                        obstacles.append((i, 6))
                        obstacles.append((i, 14))
            case 14:
                for row in range(4, 17, 3):      # Spaced every 3 tiles vertically
                    for col in range(4, 17, 3):  # Spaced every 3 tiles horizontally
                        # Keep the center 3x3 pocket empty for safe snake resets
                        if not (7 <= row <= 12 and  7 <= col <= 12):
                            obstacles.append((row, col))
            case 15:
                # Long horizontal lines
                obstacles = addVerticalBar(16, 6, 2)
                obstacles.extend(addVerticalBar(16, 14, 2))
                obstacles.extend(addVerticalBar(16, 4, 2))
                obstacles.extend(addVerticalBar(16, 16, 2))
                obstacles.extend(addVerticalBar(16, 8, 2))
                obstacles.extend(addVerticalBar(16, 12, 2))
            case 16:
                # Long vertical lines
                obstacles = addHorizontalBar(16, 2, 5)
                obstacles.extend(addHorizontalBar(16, 2, 15))
                obstacles.extend(addHorizontalBar(16, 2, 3))
                obstacles.extend(addHorizontalBar(16, 2, 17))
                obstacles.extend(addHorizontalBar(16, 2, 7))
                obstacles.extend(addHorizontalBar(16, 2, 13))
            case 17:
                # The labyrinth
                # Horizontals
                # Outermost Layer
                obstacles = addVerticalBar(12, 2, 4)
                obstacles.extend(addVerticalBar(12, 17, 4))
                # Second Layer
                obstacles.extend(addVerticalBar(8, 4, 6))
                obstacles.extend(addVerticalBar(8, 15, 6))
                # Third Innermost Layer
                obstacles.extend(addVerticalBar(4, 6, 8))
                obstacles.extend(addVerticalBar(4, 13, 8))

                # Verticals
                # Outermost Layer
                obstacles.extend(addHorizontalBar(12, 4, 2))
                obstacles.extend(addHorizontalBar(12, 4, 17))
                # Second Layer
                obstacles.extend(addHorizontalBar(8, 6, 4))
                obstacles.extend(addHorizontalBar(8, 6, 15))
                # Third Innermost Layer
                obstacles.extend(addHorizontalBar(4, 8, 6))
                obstacles.extend(addHorizontalBar(4, 8, 13))
            case 18:
                # Nine crosses
                # Top row
                # Top left cross
                obstacles = addHorizontalBar(3, 2, 3)
                obstacles.extend(addVerticalBar(3, 3, 2))
                # Top center cross
                obstacles.extend(addHorizontalBar(3, 8, 3))
                obstacles.extend(addVerticalBar(3, 9, 2))
                # Top right cross
                obstacles.extend(addHorizontalBar(3, 14, 3))
                obstacles.extend(addVerticalBar(3, 15, 2))
                
                # Middle row
                # Mid left cross
                obstacles.extend(addHorizontalBar(3, 2, 9))
                obstacles.extend(addVerticalBar(3, 3, 8))
                # Mid center cross
                obstacles.extend(addHorizontalBar(3, 8, 9))
                obstacles.extend(addVerticalBar(3, 9, 8))
                # Mid right cross
                obstacles.extend(addHorizontalBar(3, 14, 9))
                obstacles.extend(addVerticalBar(3, 15, 8))
                
                # Bottom row
                # Bottom left
                obstacles.extend(addHorizontalBar(3, 2, 15))
                obstacles.extend(addVerticalBar(3, 3, 14))
                # Bottom center
                obstacles.extend(addHorizontalBar(3, 8, 15))
                obstacles.extend(addVerticalBar(3, 9, 14))
                # Bottom right
                obstacles.extend(addHorizontalBar(3, 14, 15))
                obstacles.extend(addVerticalBar(3, 15, 14))
            case 19:
                # Boxes around a vault
                obstacles = addHorizontalBar(4, 8, 6)
                obstacles.extend(addHorizontalBar(4, 8, 13))
                obstacles.extend(addBox(4, 3, 3))
                obstacles.extend(addBox(4, 13, 13))
                obstacles.extend(addBox(4, 3, 13))
                obstacles.extend(addBox(4, 13, 3))
                obstacles.extend(addVerticalBar(4, 6, 8))
                obstacles.extend(addVerticalBar(4, 13, 8))
            case 20:
                # Checker board
                new_obstacles = []
                # Loop through the board matrix, skipping the outer boundary
                for r in range(2, 20 - 2):
                    for c in range(2, 20 - 2):
                        # Check if row and column indices create a alternating checker pattern
                        if (r % 2 == 0) and (c % 2 == 0):
                            # Avoid to make safe area for the snake to spawn
                            if (r, c) != (10, 10) and (r, c) != (10, 12) and (r, c) != (10, 8) and (r, c) != (10, 6):
                                new_obstacles.append((r, c))
                obstacles = new_obstacles
            
            case _:
                if mode == 'Classic':
                    print("end")
                else:
                    obstacles = random_level(obstacles)
                
    elif mode == 'Random':
        obstacles = random_level(obstacles)

    return obstacles
