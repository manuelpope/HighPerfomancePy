print("Numpy Introduction ")
import numpy as np

listNumber = [elem for elem in range (1,6)]


nparraylist = np.array(listNumber)


ndarray= np.array([listNumber,listNumber,listNumber])

print(ndarray[:][2], ndarray.shape)

zeroArr= np.zeros((4,4))
onesArr= np.ones((4,4))
ideMatrix= np.eye(4)
randomArr = np.random.random((4,4))
print(zeroArr,"  ",onesArr,ideMatrix,randomArr)
print(np.arange(5,15,0.5))
print(ndarray[:,:1])
print(ndarray[1:3,1:3])
print(ndarray)
print(ndarray[[0,1,2],[0,1,2]]) #diagonal

print(ndarray%2==0) #operation over a matrix

booleanMask= ndarray%2==0

print(ndarray[booleanMask]) #its a filter with numpy