from scipy.signal import hilbert
import numpy as np
import matplotlib.pyplot as plt
import statistics

t = []
A = []

tm = []
Am = []

with open('murckowskaW.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        t.append(float(row[0]))
        A.append(float(row[1]))

with open('data_4_rbin53_ZTPI.txt', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        tm.append(float(row[0]))
        Am.append(float(row[1]))
# print(t, A)

# for index, item in enumerate(t):
#     if item > 100 and item < 101:
#         print(index, item)

# print(statistics.mean(A))
# A2 = [x - statistics.mean(A) for x in A]
# t2 = t[int(0.05*len(t)):int(0.95*len(t))]
# A3 = A2[int(0.05*len(t)):int(0.95*len(t))]

# amplitude_envelope = np.abs(hilbert(A3))

fig, ax = plt.subplots()
ax.plot(t, A)
# ax.plot(t2, amplitude_envelope)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
plt.show()

fig, ax = plt.subplots()
ax.plot(tm, Am)
# ax.plot(t2, amplitude_envelope)
ax.set_xlabel('Time')
ax.set_ylabel('Amplitude')
plt.show()
