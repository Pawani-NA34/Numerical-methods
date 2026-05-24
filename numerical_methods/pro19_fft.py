
'''#%%'''

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
f = np.exp(-x**2)

F = np.fft.fft(f)
freqs = np.fft.fftfreq(len(x), d=x[1]-x[0])

# center frequency axis (normal for FFT viewing)
freqs = np.fft.fftshift(freqs)
F = np.fft.fftshift(F)

plt.plot(freqs, np.abs(F))
plt.xlabel("frequency")
plt.ylabel("magnitude")
# plt.savefig("fft_plot.png")
# print("saved!")

plt.show()