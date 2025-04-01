import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# Set your grid size here (e.g., 4, 8, etc.)
GRID_SIZE = 4
species_count = 4
steps = 300

plant_names = ['Rose', 'Tulip', 'Sunflower', 'Lavender']
plant_colors = ['red', 'yellow', 'orange', 'purple']
cmap = ListedColormap(plant_colors)


grid = np.random.randint(0, species_count, size=(GRID_SIZE, GRID_SIZE))

# Toroidal neighbor function
def get_neighbors(r, c):
    return [
        ((r - 1) % GRID_SIZE, c),
        ((r + 1) % GRID_SIZE, c),
        (r, (c - 1) % GRID_SIZE),
        (r, (c + 1) % GRID_SIZE)
    ]

# One simulation step
def step(grid):
    r, c = np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE)
    neighbors = get_neighbors(r, c)
    nr, nc = neighbors[np.random.randint(0, len(neighbors))]
    grid[nr, nc] = grid[r, c]
    return grid

# Plot setup
fig, ax = plt.subplots(figsize=(5, 5))
img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=species_count - 1)

# Hide axis ticks and labels
ax.set_xticks([])
ax.set_yticks([])

# Optional: show grid lines between cells
ax.set_xticks(np.arange(-0.5, GRID_SIZE, 1), minor=True)
ax.set_yticks(np.arange(-0.5, GRID_SIZE, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=0.5)
ax.tick_params(which='minor', bottom=False, left=False)

# Colorbar (legend)
cbar = plt.colorbar(img, ticks=range(species_count), ax=ax)
cbar.ax.set_yticklabels(plant_names)


ax.set_title("Stepping Stone Simulation")

# Animation update function
def update(frame):
    global grid
    grid = step(grid.copy())
    img.set_array(grid)
    ax.set_title(f"Step {frame + 1}")
    return [img]

# Create and save animation
plt.tight_layout()
ani = animation.FuncAnimation(fig, update, frames=steps, interval=300, repeat=False)
ani.save("stepping_stone_simulation.mp4", writer='ffmpeg')
print("Animation saved as stepping_stone_simulation.mp4")
