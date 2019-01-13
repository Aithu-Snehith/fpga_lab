import soundfile as sf
from scipy import signal

#read .wav file
# input_signal,fs = sf.read('Sound_Noise.wav')
# print input_signal.shape
#sampling frequency of Input signal
sampl_freq=1e4

#order of the filter
order=4

#cutoff frquency 4kHz
cutoff_freq=300.0

#digital frequency
Wn=2*cutoff_freq/sampl_freq

# b and a are numerator and denominator polynomials respectively
b, a = signal.butter(order,Wn, 'low')
print a,b
#filter the input signal with butterworth filter
# output_signal = signal.filtfilt(b, a, [1])
#
# #write the output signal into .wav file
# sf.write('ht.wav', output_signal, fs)
