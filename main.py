import pygame
import sys

# Initialize pygame
pygame.init()

# Define the maze
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the size of the maze and cells
maze_width = len(maze[0])
maze_height = len(maze)
cell_size = 50

# Define the size of the window
window_width = maze_width * cell_size
window_height = maze_height * cell_size

# Create the window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Goal-Based Maze Game")

# Set the initial player position and goal position
player_pos = (1, 1)
goal_pos = (maze_height - 2, maze_width - 2)

# Define the utilities for each state in the maze
utilities = [
    [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100],
    [-100, 0, 0, 0, 0, 0, 0, 0, 0, -100],
    [-100, 0, -100, -100, -100, -100, -100, -100, 0, -100],
    [-100, 0, -100, 0, 0, 0, 0, -100, 0, -100],
    [-100, 0, -100, 0, -100, -100, 0, -100, 0, -100],
    [-100, 0, -100, 0, -100, -100, 0, -100, 0, -100],
    [-100, 0, -100, 0, 0, 0, 0, -100, 0, -100],
    [-100, 0, -100, -100, -100, -100, -100, -100, 0, -100],
    [-100, 0, +5000, 0, 0, 0, 0, 0, +1000, -100],
    [-100, -100, -100, -100, -100, -100, -100, -100, -100, -100]
]

# Function to draw the maze and the player
def draw_maze():
    window.fill(BLACK)

    for row in range(maze_height):
        for col in range(maze_width):
            if maze[row][col] == 1:
                pygame.draw.rect(window, WHITE, (col * cell_size, row * cell_size, cell_size, cell_size))
            elif maze[row][col] == 0:
                pygame.draw.rect(window, BLUE, (col * cell_size, row * cell_size, cell_size, cell_size))

    pygame.draw.rect(window, BLACK, (player_pos[1] * cell_size, player_pos[0] * cell_size, cell_size, cell_size))
    pygame.draw.rect(window, RED, (goal_pos[1] * cell_size, goal_pos[0] * cell_size, cell_size, cell_size))

    pygame.display.update()

# Function to handle player movement
def move_player(dx, dy):
    new_pos = (player_pos[0] + dy, player_pos[1] + dx)
    print(new_pos)

    if maze[new_pos[0]][new_pos[1]] == 0:
        return new_pos
    else:
        return player_pos

# Calculate the utility for reaching the goal state (MEU)
def calculate_utility():
    return utilities[goal_pos[0]][goal_pos[1]]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_pos = move_player(0, -1)
            elif event.key == pygame.K_DOWN:
                player_pos = move_player(0, 1)
            elif event.key == pygame.K_LEFT:
                player_pos = move_player(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player_pos = move_player(1, 0)

    draw_maze()

    # Check if the player reached the goal
    if player_pos == goal_pos:
        print("Congratulations! You reached the goal!")
        utility = calculate_utility()
        print("Utility for reaching the goal:", utility)
        pygame.quit()
sys.exit()
