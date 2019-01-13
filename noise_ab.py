import soundfile as sf
from scipy import signal

input_signal,fs = sf.read('Sound_Noise.wav')

#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=4000.0

#digital frequency
Wn=2.0*cutoff_freq/fs

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low')
print a
print b
