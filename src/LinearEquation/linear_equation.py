import numpy as np
import matplotlib.pyplot as plt

# First three values of the RU
a = 4
b = 5
c = 4

# Create a random vector of 10 elements for the values of x
np.random.seed(42)
x = np.random.rand(10)

# Apply the values to the function and calculate the results
y = a * x + b * x - c

# Plot the points (results)
plt.scatter(x, y, c='blue', label='Points')

# Legend and axis labels
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Display the graph
plt.show()
