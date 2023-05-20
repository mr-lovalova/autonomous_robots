import numpy as np

## Kalman Filter:
# Consider a constant velocity model and the state and covariance are the following:
x = 3  # position in x axis
x_ = 0.5  # x': velocity in x axis
y = 2  # position in y axis
y_ = 0.33  # y': velocity in in y axis

cov_matrix = np.array([[5, 1, 0, 0], [1, 2, 0, 0], [0, 0, 5, 1], [0, 0, 1, 2]])
# measurement = [4.8,7.1]
# we assumed that is only position because velocity
# is constant as indicated in the statement. Furthermore, we consider
# that the values correspond to the axis "x" and "y" respectively

# observed Noise:
R = 1
# What is the state after having **updated** it with the current measurement?
# (**don't run the predict step, only the update step**)


# **Solution:**

# Let's first set the interest matrices, and then adapt the functions of the
# exercise 2d, week7 (monday) for only one step of measurements


# The initial state. The robot starts in position 0 with the velocity 0.
x = np.array(
    [
        [3],  # Position along the x-axis
        [0.5],  # Velocity along the x-axis
        [2],  # Position along the y-axis
        [0.33],
    ]
)  # Velocity along the y-axis

### Update the rest of the parameters

# The initial uncertainty. We consider the values given by the covariance matrix.
P = cov_matrix

# The external motion. Set to 0 here.
u = np.array([[0], [0], [0], [0]])

# The transition matrix. Based on the relationship given by motion ecuations:
F = np.array([[1, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 1], [0, 0, 0, 1]])

# The observation matrix. We only get the position as measurement.
H = np.array([[1, 0, 0, 0], [0, 0, 1, 0]])

# The measurement uncertainty
R = np.array([[0.2, 0.2], [0.2, 0.2]])

# The identity matrix. Simply a matrix with 1 in the diagonal and 0 elsewhere.
I = np.identity(4)


def predict(x, P, F, u):  # for motion
    ## insert predict function

    # Predicting P
    P_p = np.linalg.multi_dot([F, P, F.T])

    # Predicting x
    x_p = np.dot(F, x) + u

    return x_p, P_p


x_p, P_p = predict(x, P, F, u)
print("x_p:")
print(x_p)
print()
print("P_p")
print(P_p)
