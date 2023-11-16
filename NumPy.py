import numpy as np   #replace numpy as np for eiserser reuse

a1 = np.array([1,2,3,4])

a2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

a3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,2,3,4],[5,6,7,8],[9,10,11,12]])

im = np.identity(3)

ie = np.eye(3)

a0 = np.zeros(4)

a20 = np.zeros((2,3))

a30 = np.zeros((2,3))

a21 = np.full((2,3),1)

grades = np.loadtxt('grade.txt')




grades = np.loadtxt('gardes.txt')
grades = np.loadtxt('twodArray.txt',ndmin = 1)

data = np.loadtxt('twodArray.txt',ndmin = 1)
x = np.zeros(len(data))
m = np.zeros(len(data))

for i in range (0,len(data)):
    x[i] = data[i][0]
    m[i] = data[i][1]


m1 = m + 0.1

import matplotib.pyploy as plt





