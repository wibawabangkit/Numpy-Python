import numpy as np


a = np.floor(np.random.randn(2,2)*10)
print(a)
#cara sorting nilai maximum
print('nilai max dari a = ',a.max())
print ('posisi max dari a =',a.argmax())
#cara sorting nilai minimum
print('nilai min dari a = ',a.min())
print ('posisi min dari a =',a.argmin())
#mengurutkan nilai a
print('mengurutkan nilai a = ')
print(np.sort(a))
print(np.argsort(a))