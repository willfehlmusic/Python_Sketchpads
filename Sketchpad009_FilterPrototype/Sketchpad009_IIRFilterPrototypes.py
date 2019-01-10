import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# create a relatively long impulse response
inputSignal = np.zeros(2048)
# make the first sample == 1
inputSignal[0] = 1
# use this container to get a copy of the b and a coefficiencts for each 4th order filter
filterSystems = []




# ---------- butterworth filter ----------
bArray = [] # for b coeffecients
aArray = [] # for a coeffecients
wArray = [] # for omega
hArray = [] # for H
orderArray = [1, 2, 4, 5] # orders to use
omega_c = 0.25 # cutoff frequency

for i in orderArray:
    b, a = signal.butter(N=i, Wn=omega_c)
    if i == 4:
        filterSystems.append([b,a])
    w, h = signal.freqz(b, a)
    bArray.append(b)
    aArray.append(a)
    wArray.append(w)
    hArray.append(h)

fig = plt.figure(figsize=(16, 9))
for index in range(len(orderArray)):
    plt.plot(wArray[index], 20 * np.log10(abs(hArray[index])), label="order = " + str(orderArray[index]))
plt.title('Butterworth Filter Frequency Response: Comparison')
plt.xlabel('Frequency [up to Nyquist]')
plt.xlim([0, np.pi])
plt.ylim([-60, 12])
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.axvline(omega_c*np.pi, color='black') # cutoff frequency
plt.legend()
plt.savefig('Butterworth.png')




# ---------- chebyshev 1 ----------
bArray = []
aArray = []
wArray = []
hArray = []
orderArray = [1, 2, 4, 5]
omega_c = 0.25
for i in orderArray:
    b, a = signal.cheby1(N=i, rp=6, Wn=omega_c)
    if i == 4:
        filterSystems.append([b,a])
    w, h = signal.freqz(b, a)
    bArray.append(b)
    aArray.append(a)
    wArray.append(w)
    hArray.append(h)

fig = plt.figure(figsize=(16, 9))
for index in range(len(orderArray)):
    plt.plot(wArray[index], 20 * np.log10(abs(hArray[index])), label="order = " + str(orderArray[index]))
plt.title('Chebyshev Type 1 Filter Frequency Response: Comparison')
plt.xlabel('Frequency [up to Nyquist]')
plt.xlim([0, np.pi])
plt.ylim([-60, 12])
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.axvline(omega_c*np.pi, color='black') # cutoff frequency
plt.legend()
plt.savefig('ChebyshevT1.png')




# ---------- chebyshev 2 ----------
bArray = []
aArray = []
wArray = []
hArray = []
orderArray = [1, 2, 4, 5]
omega_c = 0.25
for i in orderArray:
    b, a = signal.cheby2(N=i, rs=54, Wn=omega_c)
    if i == 4:
        filterSystems.append([b,a])
    w, h = signal.freqz(b, a)
    bArray.append(b)
    aArray.append(a)
    wArray.append(w)
    hArray.append(h)

fig = plt.figure(figsize=(16, 9))
for index in range(len(orderArray)):
    plt.plot(wArray[index], 20 * np.log10(abs(hArray[index])), label="order = " + str(orderArray[index]))
plt.title('Chebyshev Type 2 Filter Frequency Response: Comparison')
plt.xlabel('Frequency [up to Nyquist]')
plt.xlim([0, np.pi])
plt.ylim([-60, 12])
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.axvline(omega_c*np.pi, color='black') # cutoff frequency
plt.legend()
plt.savefig('ChebyshevT2.png')




# ---------- elliptic ----------
bArray = []
aArray = []
wArray = []
hArray = []
orderArray = [1, 2, 4, 5]
omega_c = 0.25
for i in orderArray:
    b, a = signal.ellip(N=i, rp=6, rs=54, Wn=omega_c)
    if i == 4:
        filterSystems.append([b,a])
    w, h = signal.freqz(b, a)
    bArray.append(b)
    aArray.append(a)
    wArray.append(w)
    hArray.append(h)

fig = plt.figure(figsize=(16, 9))
for index in range(len(orderArray)):
    plt.plot(wArray[index], 20 * np.log10(abs(hArray[index])), label="order = " + str(orderArray[index]))
plt.title('Elliptic Filter Frequency Response: Comparison')
plt.xlabel('Frequency [up to Nyquist]')
plt.xlim([0, np.pi])
plt.ylim([-60, 12])
plt.ylabel('Amplitude [dB]')
plt.grid(which='both', axis='both')
plt.axvline(omega_c*np.pi, color='black') # cutoff frequency
plt.legend()
plt.savefig('Elliptic.png')




# ---------- graph the impulse responses ----------
names = ["Butterworth","Chebyshev T1","Chebyshev T2","Elliptic"]
fig = plt.figure(figsize=(16, 9))
nameIndex = 0
for coef in filterSystems:
    fImpulse = signal.lfilter(coef[0], coef[1], inputSignal) # calculate impulse response
    plt.plot(fImpulse, label=names[nameIndex])
    nameIndex += 1
plt.title('Compare 4th Order Filter Impulse Response')
plt.xlabel('Time [samples]')
plt.xlim([0, 128])
plt.ylabel('Amplitude')
plt.grid(which='both', axis='both')
plt.legend()
plt.savefig('CompareFilterTime.png')


