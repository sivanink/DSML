import matplotlib.pyplot as plt
import numpy as np
x=np.array([88,92,80,89,100,80,60,100,80,34])
y = np.array([35,79,79,48,100,88,32,45,20,30])
plt.scatter(x,y)
plt.xlabel("Maths")
plt.ylabel("Science")
plt.title("Scatter Plot")
plt.grid(True)
plt.show()
