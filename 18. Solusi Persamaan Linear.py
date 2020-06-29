import numpy as np

#persamaan linier
A = np.array([(2,3),(1,2)])
Y = np.array([23,14])
print(A)
print(Y)

A_inv = np.linalg.inv(A)
#menelesaikan persamaan linier
X = np.dot(A_inv,Y)
print(X)

#cara lain
X2 = np.linalg.solve(A,Y)
print(X2)
