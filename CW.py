#to import numpy and rename to np for easier reuse
import numpy as np

windData = np.loadtxt('windturbinepower.txt') #to load and read the data from the txt file

#print (windData)


maxVal = np.amax(windData) #to find the maximum value from the txt file

print ("Maximum Value: ",maxVal)
print ()

meanVal = np.mean(windData) #to find the mean value of all data from the txt file

print ("Mean: ",windData)
print ()


stdVal = np.std(windData)

print ("Standard Deviation: ",windData)  #to find the standard deviation of all data from the txt file

#to import the matplotlib and rename to plt for eaier reuse
import matplotlib.pyplot as plt

graph = plt.figure(1)

windData = np.loadtxt('windturbinepower.txt')
time = np.linspace(0,10,50001)

plt.plot(time,windData,'-+r')
plt.title ('wind turbine power')
plot.xlabel('time/s')
plot.ylabel('power/W')
plt.show


