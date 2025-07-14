import numpy as np

# Define a 2x2 matrix
matrix = np.array([[1, 2],
                   [3, 4]])

# Calculate the inverse
inverse_matrix = np.linalg.inv(matrix)

# Print the results
print("Matrix:")
print(matrix)

print("\nInverse:")
print(inverse_matrix)
