import numpy as np

print("Enter elements:")
a=input("Enter element 1:")
b=input("Enter element 2:")
c=input("Enter element 3:")
d=input("Enter element 4:")
s=np.array([[int (a),int (b)],[int (c),int (d)]])
print(s)
inv=np.linalg.inv(s)
print(inv)
