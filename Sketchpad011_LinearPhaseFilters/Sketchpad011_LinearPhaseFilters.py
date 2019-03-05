import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

fs = 48000

fc = 1000/(fs/2)
bHamming = signal.firwin(numtaps=128,cutoff=fc)
bBlackmanHarris = signal.firwin(numtaps=128,cutoff=fc, window='blackmanharris')
bButterworth, aButterworth = signal.iirfilter(8, fc, btype='lowpass', ftype='butter')
bEllip, aEllip = signal.iirfilter(8, fc, rp=1, rs=54,  btype='lowpass', ftype='ellip')
print(len(aButterworth))
print(len(bButterworth))
print(len(aEllip))
print(len(bEllip))
coeffArray = [[bHamming, [1]], [bBlackmanHarris, [1]], [bButterworth, aButterworth], [bEllip, aEllip]]
labels = ["Hamming", "Blackman-Harris", "Butterworth", "Elliptic"]

fig = plt.figure(figsize=(16, 9))
plt.title("Compare Different Filters")
for e in range(len(coeffArray)):
    fCoef = coeffArray[e]
    w, h = signal.freqz(fCoef[0], fCoef[1])
    plt.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), label=labels[e])
plt.xlabel('Magnitude [dB]')
plt.ylabel('Frequency [Hz]')
plt.ylim([-120, 12])
plt.xlim([20, 20000])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("CompareFilters.png")

for e in range(len(coeffArray)):
    fig, ax1 = plt.subplots()
    ax1.set_title(labels[e] + ' : Digital Filter Frequency Lin Scale')
    fCoef = coeffArray[e]
    w, h = signal.freqz(fCoef[0], fCoef[1])
    w = w[0:100]
    h = h[0:100]
    ax1.plot((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), 'b')
    ax1.set_ylabel('Magnitude [dB]', color='b')
    ax1.set_xlabel('Frequency [Hz]')
    ax1.grid()
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.plot((fs / 2) * (w / np.pi), angles, 'r')
    ax2.set_ylabel('Angle (radians)', color='r')
    ax2.axis('tight')
    ax2.grid()
    plt.savefig(labels[e] + "FrequencyPhaseLinScale.png")

for e in range(len(coeffArray)):
    fig, ax1 = plt.subplots()
    ax1.set_title(labels[e] + ' : Digital Filter Frequency Log Scale')
    fCoef = coeffArray[e]
    w, h = signal.freqz(fCoef[0], fCoef[1])
    ax1.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), 'b')
    ax1.set_ylabel('Magnitude [dB]', color='b')
    ax1.set_xlabel('Frequency [Hz]')
    ax1.grid()
    ax2 = ax1.twinx()
    angles = np.unwrap(np.angle(h))
    ax2.semilogx((fs / 2) * (w / np.pi), angles, 'r')
    ax2.set_ylabel('Angle (radians)', color='r')
    ax2.axis('tight')
    ax2.grid()
    plt.savefig(labels[e] + "FrequencyPhaseLogScale.png")



tSecond = 0.5 # time in second
tVec = np.linspace(0,tSecond, tSecond*fs)

osc0 = np.sin(2 * np.pi * fs * 100 * tVec)
osc1 = 0.5 * np.sin(2 * np.pi * fs * 350 * tVec)
osc2 = 0.25 * np.sin(2 * np.pi * fs * 503 * tVec)
signalClean = (osc0+osc1+osc2)/2

signalHamming = signal.lfilter(coeffArray[0][0], coeffArray[0][1], signalClean)
signalBlackmanHarris = signal.lfilter(coeffArray[1][0], coeffArray[1][1], signalClean)
signalButterworth = signal.lfilter(coeffArray[2][0], coeffArray[2][1], signalClean)
signalElliptic = signal.lfilter(coeffArray[3][0], coeffArray[3][1], signalClean)

fig = plt.figure(figsize=(20, 9))
plt.title('Digital filter frequency response')
plt.subplot(511)
plt.plot(tVec, signalClean)
plt.title("Clean")
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.xlim([0, 0.04])
plt.ylim([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.subplot(512)
plt.plot(tVec, signalClean)
plt.plot(tVec, signalHamming)
plt.title("Hamming")
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.xlim([0, 0.04])
plt.ylim([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.subplot(513)
plt.plot(tVec, signalClean)
plt.plot(tVec, signalBlackmanHarris)
plt.title("Blackman-Harris")
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.xlim([0, 0.04])
plt.ylim([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.subplot(514)
plt.plot(tVec, signalClean)
plt.plot(tVec, signalButterworth)
plt.title("Butterworth")
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.xlim([0, 0.04])
plt.ylim([-1, 1])
plt.grid(True)
plt.tight_layout()
plt.subplot(515)
plt.plot(tVec, signalClean)
plt.plot(tVec, signalElliptic)
plt.title("Elliptic")
plt.xlabel('Amplitude')
plt.ylabel('Time')
plt.xlim([0, 0.04])
plt.ylim([-1, 1])
plt.grid(True)
plt.tight_layout()

plt.savefig("EffectTimeDomain.png")



