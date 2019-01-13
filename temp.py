import numpy as np
import soundfile as sf

input_signal,fs = sf.read('Sound_Noise.wav')

output_signal = np.genfromtxt("test.txt")
sf.write('cleaned.wav', output_signal, fs)

print "done"
