import numpy as np

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2,3],[4,5,6]])
print ("First Array:",a)
print ("Second Array:",b)
if np.array_equal(a,b):
	print ("Equal")
else:
	print("Not Equal!")

