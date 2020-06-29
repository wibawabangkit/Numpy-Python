import numpy as np 


a1 = np.array(([1,2,3],
                [4,5,6]))

print('matrix a1 dengan ukuran:', a1.shape)
print(a1)



#reshape matrix
print("reshape matrix a1:")
print(a1.reshape(3,2))
print('matrix a1 dengan ukuran:',a1.shape)