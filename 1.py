import numpy as np
import matplotlib.pyplot as plt
import subprocess
import shlex

#RC filter frequency response
def H(f):
	s = 1j*2*np.pi*f
	den = np.polyval([1,1],s*C*R)
	H = 1/den
	return H


#Filter Characteristics

R = 50; #500 ohm resistance
C = 10e-6;#10 uF capacitance

#Plotting the filter amplitude response
f_0 = 50.0
f = np.linspace(-1*f_0,6*f_0,1e2)

plt.plot(f,abs(H(f)))
print abs(H(5000))
print abs(H(10))
plt.grid()# minor
plt.xlabel('$f$ (Hz)')
plt.ylabel('$H(f)$')
#Save figure
#plt.savefig('../figs/lpf.eps')
#plt.savefig('../figs/lpf.pdf')
#subprocess.run(shlex.split("termux-open ../figs/lpf.pdf"))
plt.show()
