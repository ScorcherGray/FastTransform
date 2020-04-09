# Homework 9
# Signal corrupted by noise.
# x(t) = A1sin(2pif1t) + A2sin(2pif2t) + noise
# 1: Create a program that reads in the file and plots it as a function of time.
import matplotlib.pyplot as plt
import numpy as np

def read(txt):
    return_list = []
    for line in txt:
        return_list.append(float(line.strip()))
    return return_list

wave = open("waveform.txt", "r")
values = read(wave)
timeList = [t for t in range(len(values))] # for each item in the list, save 0:n
fs = 1500
ts = 1/fs
sample_length = len(values)

noisy = np.fft.fft(values)
half = int(sample_length/2)
p2 = np.abs(noisy / sample_length)
p1 = p2[:half]
p1[1:-2] = 2*p1[1:-2]

ps = int(fs/sample_length)
spectrum = [ps * idx for idx in range(half)]

# number 3
a1 = 0.96
f1 = 32
a2 = 1.37
f2 = 67

fixed_noise = np.fix([(x/.5).real for x in noisy])*.5
ifft_fcn = np.fft.ifft(fixed_noise)

plt.figure("1")
plt.title("Number 1")
plt.plot(timeList, values)

plt.figure("2")
plt.title("Number 2")
plt.plot(spectrum, p1)

plt.figure("4")
plt.title("Number 4")
plt.plot(timeList, ifft_fcn)
plt.show()