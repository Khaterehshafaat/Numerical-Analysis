import numpy as np



P = np.array([
    [0.999967, 0.000033],
    [0.0,      1.0     ]
])


Q = np.array([[0.999967]])  # Only one transient state: Alive


I = np.eye(Q.shape[0])
N = np.linalg.inv(I - Q)


expected_days = np.sum(N)

# Convert days to years 
expected_years = expected_days / 365.25


print(f"Expected lifespan in days: {expected_days:.2f}")
print(f"Expected lifespan in years: {expected_years:.2f}")
