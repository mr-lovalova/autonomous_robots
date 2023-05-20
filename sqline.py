import numpy as np
from numpy import cos, sin, arctan2
import matplotlib.pyplot as mp


def get_line(distances, angles):
    line = []
    for count, _ in enumerate(distances):
        r, a = distances[count], np.radians(angles[count])
        p = (r * cos(a), r * sin(a))
        line.append(p)
    return line


if __name__ == "__main__":
    angles = [90, 45, 0, -45]
    dist = [4.5, 2.1, 2.4, 6.3]
    line = get_line(dist, angles)
    x = []
    y = []
    for point in line:
        x.append(point[0])
        y.append(point[1])
    m, b = np.polyfit(x, y, 1)

    theta = np.arctan2(m, 1)
    r = b / np.sin(theta)
    theta = np.degrees(theta)

    psum = 0
    for i in range(len(dist)):
        psum += cos()
    psum = psum(len(dist))
    print(psum)
    alpha = 
    print(r, theta)
