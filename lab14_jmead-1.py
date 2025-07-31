"""
Circumference of a Circle
John Mead
This program will graph a circle using it's radius.
7-29-25
"""

import math
import matplotlib.pyplot as plt


radius = 5
x_coords = []
y_coords = []


for degree in range(360):
    radians = math.radians(degree)

    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    x_coords.append(x)
    y_coords.append(y)


plt.plot(x_coords, y_coords, color = 'purple', linewidth = 2, linestyle = '--')
plt.axis('equal')
plt.title("Circumference of a Circle")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()