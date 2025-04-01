import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import random
from statistics import mean
import matplotlib

# Use Agg backend for headless environments (optional if running locally)
matplotlib.use("Agg")

# Parameters
GRID_SIZE = 8
start = (1, 1)
target = (8, 8)
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
num_simulations = 50
video_path = "bob_random_walk.mp4"  # Output file

# Check if position is valid
def is_valid(pos):
    return 1 <= pos[0] <= GRID_SIZE and 1 <= pos[1] <= GRID_SIZE

# Simulate one random walk
def simulate_random_walk_grid():
    path = [start]
    current = start
    while current != target:
        valid_moves = [move for move in moves if is_valid((current[0] + move[0], current[1] + move[1]))]
        move = random.choice(valid_moves)
        current = (current[0] + move[0], current[1] + move[1])
        path.append(current)
    return path

# Run simulations
paths = []
steps_list = []
for _ in range(num_simulations):
    path = simulate_random_walk_grid()
    paths.append(path)
    steps_list.append(len(path) - 1)

# Create a table of first 10 simulation paths
sim_df = pd.DataFrame({
    f'Simulation {i+1}': [str(pos) for pos in paths[i]] + [None]*(max(len(p) for p in paths) - len(paths[i]))
    for i in range(min(num_simulations, 10))
})
print("\n--- First 10 Simulated Paths ---\n")
print(sim_df)

# Calculate and show average steps
average_steps = mean(steps_list)
print(f"\nAverage steps to reach target over {num_simulations} simulations: {average_steps:.2f}")

# Create animation for the first path
selected_path = paths[0]
fig, ax = plt.subplots(figsize=(6, 6))
grid = np.zeros((GRID_SIZE, GRID_SIZE))
img = ax.imshow(grid, cmap='Greens', vmin=0, vmax=2)

target_r, target_c = target
grid[target_r - 1, target_c - 1] = 2

def update(frame):
    grid = np.zeros((GRID_SIZE, GRID_SIZE))
    for i in range(frame + 1):
        r, c = selected_path[i]
        grid[r - 1, c - 1] = 1
    grid[target_r - 1, target_c - 1] = 2
    img.set_array(grid)
    ax.set_xticks(range(GRID_SIZE))
    ax.set_yticks(range(GRID_SIZE))
    ax.set_title(f"Step {frame + 1} / {len(selected_path)}")
    return [img]

ani = animation.FuncAnimation(fig, update, frames=len(selected_path), interval=200, repeat=False)
ani.save(video_path, writer='ffmpeg')
plt.close()

print(f"\nAnimation saved as: {video_path}")

# Save the first 10 simulations to an Excel file
excel_path = "random_walk_simulations.xlsx"
sim_df.to_excel(excel_path, index=False)
print(f"\nExcel file saved as: {excel_path}")

