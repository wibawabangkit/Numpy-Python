import numpy as np 



aa = np.array ([1,2,3])
bb = np.array ([4,5,6])


aaMat = np.zeros((2,3))
bbMat = np.ones((2,3))

#stacking matrix, menumpuk matrix

cc = np.hstack ((aa,bb))
dd = np.vstack ((aa,bb))

ccMat = np.hstack((aaMat,bbMat))
ddMat = np.vstack((aaMat,bbMat))

print(ddMat)


