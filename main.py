from scipy.signal import hilbert
import numpy as np
import matplotlib.pyplot as plt

sensor = np.loadtxt('signal.txt')
analytical_signal = hilbert(sensor)
amplitude_envelope = np.abs(analytical_signal)

fig, ax = plt.subplots()
ax.plot(sensor)
ax.plot(amplitude_envelope)
plt.show()

t = []
A = []
with open('ztpi_data.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        t.append(float(row[0]))
        A.append(float(row[1]))

fig, ax = plt.subplots()
ax.plot(t, A)
# ax.plot(amplitude_envelope)
plt.show()
