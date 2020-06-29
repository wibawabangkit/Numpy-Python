import numpy as np

dtipe = [('nama','S10'),('tinggi',int)]
data = [

    ('ucup',170),
    ('otong',150),
    ('mario',100)
]
print ("mengurutkan data berdasarkan tipe data=")
a = np.array(data, dtype = dtipe )
print(a)
print("mengurutkan data berdasarkan tinggi =")
print(np.sort(a, order ='tinggi'))
print("mengurutkan berdasarkan abjad nama = ")
print(np.sort(a, order= 'nama'))