import numpy as np

a = np.array([(1,-1),(1,1)])
print("matrix a =")
print(a)

#invers matrix
a_inv = np.linalg.inv(a)

print("invers matrix a =")
print (a_inv)
print("invers matrix a menjadi satuan =")
print (np.dot(a,a_inv))

#determinan matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)
print("Determinan matrix a =")
print(det_a)
print("Invers Detrminan matrix a =")
print(det_a_inv)

# gunanya kita dapat menyelesaikan persamaan linier