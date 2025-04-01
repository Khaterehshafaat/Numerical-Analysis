import numpy as np

def simulate_bob_life_split_second(prob_alive_per_tick=0.99999999999988426,  # Adjusted for 0.999967/day to 10Hz ticks
                                   max_ticks=100 * 365 * 864000,         # 100 years in tenths of seconds
                                   ticks_per_year=365 * 864000):         # 864,000 tenths of a second per day
    """
    Simulate Bob's life down to the tenth of a second.
    """
    ticks_alive = 0
    current_year = 0

    print("Starting Bob's life simulation (Press CTRL+C to stop)...")

    try:
        while ticks_alive < max_ticks:
            if np.random.rand() < prob_alive_per_tick:
                ticks_alive += 1

                # Check if Bob entered a new year
                if ticks_alive // ticks_per_year > current_year:
                    current_year += 1
                    print(f" Bob just turned {current_year} years old.")
            else:
                break  # Bob died
    except KeyboardInterrupt:
        print("Simulation interrupted manually.")

    # Convert ticks back to days and years
    age_in_years = ticks_alive / ticks_per_year
    age_in_days = ticks_alive / 864000

    print(f"Bob's estimated lifespan: {age_in_years:.6f} years ({age_in_days:.2f} days)")
    print(f" Total ticks (tenths of a second): {ticks_alive}")

simulate_bob_life_split_second()
