import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print ("Orginal array:",a)

s=np.sum(a)
print ("Sum:",s)

c=np.sum(a,axis=0)
print ("Sum of columns:",c)

r=np.sum(a,axis=1)
print ("Sum of rows:",r)

