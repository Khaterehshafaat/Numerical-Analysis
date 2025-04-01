import numpy as np

def simulate_bob_life(prob_alive=0.999967, simulations=1000, max_days=100000):
    """
    Monte Carlo simulation to estimate Bob's average life expectancy.
    """
    life_lengths = []

    for _ in range(simulations):
        days_alive = 0
        while days_alive < max_days:
            if np.random.rand() < prob_alive:
                days_alive += 1  # Bob survives another day
            else:
                break  # Bob dies
        life_lengths.append(days_alive)

    return np.mean(life_lengths), life_lengths

# Run the simulation
average_life, all_lifespans = simulate_bob_life()

print(f"Estimated average life expectancy: {average_life:.2f} days")
