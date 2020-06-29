import numpy as np 


a1 = np.array(([1,2,3],
                [4,5,6]))

print('matrix a1 dengan ukuran:', a1.shape)
print(a1)


#resize matrix
print("resize matrix a1:")
a1.resize(3,2)
print(a1)
print('matrix a dengan ukuran:',a1.shape)