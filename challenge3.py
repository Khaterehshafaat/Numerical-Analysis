import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


GRID_SIZE = 8
start = (1, 1)  # Starting position (1,1)
target = (8, 8)  # Target position (8,8)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Possible moves (up, down, left, right)

# Function to check if the position is within the grid
def is_valid(pos):
    return 1 <= pos[0] <= GRID_SIZE and 1 <= pos[1] <= GRID_SIZE

# Function to simulate the random walk
def simulate_random_walk_grid():
    path = [start]
    current = start
    while current != target:  
        valid_moves = [move for move in moves if is_valid((current[0] + move[0], current[1] + move[1]))]
        move = valid_moves[np.random.randint(len(valid_moves))]  # Choose a random valid move
        current = (current[0] + move[0], current[1] + move[1])
        path.append(current)  # Append the new position to the path
    return path


path = simulate_random_walk_grid()

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
grid = np.zeros((GRID_SIZE, GRID_SIZE))  # Initialize an empty grid
img = ax.imshow(grid, cmap='Greens', vmin=0, vmax=1)  # Display the grid using a color map

# Mark the target on the grid (8, 8) as a special color for visibility
target_r, target_c = target
grid[target_r-1, target_c-1] = 2 

# Function to update the animation at each step
def update(frame):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))  
    for i in range(frame + 1):
        r, c = path[i]
        if (r, c) in [(7, 7), (8, 7)]:  
            continue
        grid[r-1, c-1] = 1
    grid[target_r-1, target_c-1] = 2
    img.set_array(grid)
    ax.set_xticks(range(GRID_SIZE))
    ax.set_yticks(range(GRID_SIZE))
    ax.set_title(f"Step {frame + 1} / {len(path)}")
    return [img]


ani = animation.FuncAnimation(fig, update, frames=len(path), interval=500, repeat=False)

ani.save("bob_random_walk.mp4", writer='ffmpeg')

print("Animation saved as bob_random_walk.mp4")
