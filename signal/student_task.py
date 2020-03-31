from scipy.signal import hilbert
import numpy as np
import matplotlib.pyplot as plt
import statistics


def plot_timeseriaes(t, A):
    fig, ax = plt.subplots()
    ax.plot(t, A)
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    plt.show()


def fft_calc(fs, A):
    fourierTransform = np.fft.fft(A) / len(A)  # Normalize amplitude
    fourierTransform = fourierTransform[range(int(len(A) / 2))]  # Exclude sampling frequency
    tpCount = len(A)
    values = np.arange(int(tpCount / 2))
    timePeriod = tpCount / fs
    frequencies = values / timePeriod
    return frequencies, fourierTransform

def plot_fft(frequencies, fourierTransform):
    # Frequency domain representation
    fig, ax = plt.subplots()
    ax.set_title('Fourier transform depicting the frequency components')
    ax.plot(frequencies, abs(fourierTransform))
    ax.set_xlabel('Frequency')
    ax.set_ylabel('Amplitude')
    plt.show()


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

for index, item in enumerate(t):
    if item > 302 and item < 303:
        print(index, item)

Aex = Am[5388:7151]
tex = tm[5388:7151]

Aex2 = A[56550:60425]
tex2 = t[56550:60425]

plot_timeseriaes(t, A)
plot_timeseriaes(tm, Am)
plot_timeseriaes(tex, Aex)
plot_timeseriaes(tex2, Aex2)

# fourierTransform = np.fft.fft(Aex) / len(Aex)  # Normalize amplitude
# fourierTransform = fourierTransform[range(int(len(Aex) / 2))]  # Exclude sampling frequency
# tpCount = len(Aex)
# values = np.arange(int(tpCount / 2))
# timePeriod = tpCount / 200
# frequencies = values / timePeriod

frequencies, fourierTransform = fft_calc(200, Aex)
plot_fft(frequencies, fourierTransform)

frequencies, fourierTransform = fft_calc(200, Aex2)
plot_fft(frequencies, fourierTransform)


# # Frequency domain representation
# fig, ax = plt.subplots()
# ax.set_title('Fourier transform depicting the frequency components')
# ax.plot(frequencies, abs(fourierTransform))
# ax.set_xlabel('Frequency')
# ax.set_ylabel('Amplitude')
# plt.show()


# fourierTransform = np.fft.fft(Aex2) / len(Aex2)  # Normalize amplitude
# fourierTransform = fourierTransform[range(int(len(Aex2) / 2))]  # Exclude sampling frequency
# tpCount = len(Aex2)
# values = np.arange(int(tpCount / 2))
# timePeriod = tpCount / 200
# frequencies = values / timePeriod
#
# # Frequency domain representation
# fig, ax = plt.subplots()
# ax.set_title('Fourier transform depicting the frequency components')
# ax.plot(frequencies, abs(fourierTransform))
# ax.set_xlabel('Frequency')
# ax.set_ylabel('Amplitude')
# plt.show()
