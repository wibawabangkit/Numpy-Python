import numpy as np 
a = np.arange(10)**2
print(a)





#perkalian matrix
a = np.array (([1,2],
                [3,4]))


b = np.ones([2,2])

print ("matrix a:")
print (a)
print(b)

c1 = np.dot(a,b)
c2 = a.dot (b)

print("matrix c:")
print(c1)


print("matrix c2:")
print(c2)


a1 = np.array(([1,2,3],
                [4,5,6]))

print('matrix a1 dengan ukuran:', a1.shape)
print(a1)
