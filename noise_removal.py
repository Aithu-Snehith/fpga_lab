import soundfile as sf
from scipy import signal
import numpy as np
import serial
import time
import matplotlib.pyplot as plt

input_signal,fs = sf.read('Sound_Noise.wav')

f = open("out_v1.txt",'w')
ser = serial.Serial('/dev/ttyACM0',9600)
count = 0
print input_signal[0]

time.sleep(5)

for i in input_signal:
	# time.sleep(0.0001)
	ser.write(str(i))
	ser.write(" ")
	y = ser.readline()
	print 'Input: ' + str(i)
	print y
	print count
	f.write(y)
	count = count + 1


f.close()

output_signal = np.genfromtxt("out_v1.txt")
sf.write('cleaned.wav', output_signal, fs)

print "done"
