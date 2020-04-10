import numpy as np


arr1= np.array([elem for elem in range (1,5)])
arr1*2
arr2 =np.array([elem for elem in range (1,5)])

print(arr1*arr2)

print(np.multiply(arr2,arr1))
randomArr1 = np.random.random((4,4))
randomArr = np.random.random((4,4))

print(np.multiply(randomArr,arr1))

# no son operaciones con matricez y las operaciones son 1to 1 ,
#  posiciona  posicion
#es mucho mas rapido numpy 14x
#------------------------------------------------------------

lg.det(randomArr)