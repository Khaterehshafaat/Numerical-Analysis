import numpy as np
import pandas as pd

# Transition matrix for the 7-block random walk
P = np.array([
    [1,    0,    0,    0,    0,    0,    0],  # Block 1 (absorbing)
    [0.5,  0,  0.5,    0,    0,    0,    0],  # Block 2
    [0,  0.5,   0,  0.5,    0,    0,    0],  # Block 3
    [0,    0, 0.5,    0,  0.5,    0,    0],  # Block 4 (starting point)
    [0,    0,   0,  0.5,    0,  0.5,    0],  # Block 5
    [0,    0,   0,    0,  0.5,    0,  0.5],  # Block 6
    [0,    0,   0,    0,    0,    0,    1]   # Block 7 (absorbing)
])

# ----------- Challenge 2a: Average duration from Block 4 -----------

def simulate_random_walk(start_block=4, simulations=10000):
    durations = []
    for _ in range(simulations):
        pos = start_block - 1  # 0-based index
        steps = 0
        while pos not in [0, 6]:  # until absorbed
            pos = np.random.choice(7, p=P[pos])
            steps += 1
        durations.append(steps)
    return np.mean(durations)

average_steps = simulate_random_walk(start_block=4)
print(f"Average number of steps until absorption from Block 4: {average_steps:.2f}")


# ----------- Challenge 2b: Block-by-block path of a single walk -----------

def single_random_walk(start_block=4, max_steps=100):
    walk_history = []
    pos = start_block - 1
    walk_history.append(pos + 1)
    steps = 0
    while pos not in [0, 6] and steps < max_steps:
        pos = np.random.choice(7, p=P[pos])
        walk_history.append(pos + 1)
        steps += 1
    return walk_history

# Run one walk and display in a table
walk = single_random_walk(start_block=4)

# Format as a DataFrame
df = pd.DataFrame({
    "Step": list(range(1, len(walk) + 1)),
    "Block": walk
})

print("\nBlock-by-block path of one random walk:")
print(df.to_string(index=False))
