import numpy as np
import serial
import time
import matplotlib.pyplot as plt

x = np.genfromtxt('input_100_1e5.csv', delimiter = ',')
print x
f = open("out_v1.txt",'w')
ser = serial.Serial('/dev/ttyACM1',9600)

for i in x[0:999]:
	ser.write(str(i))
	ser.write(" ")
	y = ser.readline()
	f.write(y)
	

#np.savetxt("output_100_1e5.csv", y, newline= ",", fmt = '%f')
f.close()

f1 = np.genfromtxt("out_v1.txt")
print(f1.shape)
print(f1)
plt.plot(f1)
plt.show()
