import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import decimal

fs = 48000

fc = 1000/(fs/2)
bBlackmanHarris = signal.firwin(numtaps=48,cutoff=fc, window='blackmanharris')
bEllip, aEllip = signal.iirfilter(6, fc, rp=3, rs=60,  btype='lowpass', ftype='ellip')
coeffArrayHighPrecision = [[bBlackmanHarris, [1]], [bEllip, aEllip]]

# convert precision
bBlackmanHarrisArrayLowerPrecision = []
bEllipArrayLowerPrecision = []
aEllipArrayLowerPrecision = []
significantFigures = 4
for b in bBlackmanHarris:
    bBlackmanHarrisArrayLowerPrecision.append(float(round(decimal.Decimal(b),significantFigures)))
for b in bEllip:
    bEllipArrayLowerPrecision.append(float(round(decimal.Decimal(b),significantFigures)))
for a in aEllip:
    aEllipArrayLowerPrecision.append(float(round(decimal.Decimal(a),significantFigures)))

coeffArrayLowerPrecision = [[bBlackmanHarrisArrayLowerPrecision, [1]], [bEllipArrayLowerPrecision, aEllipArrayLowerPrecision]]
labels = ["Blackman-Harris", "Elliptic"]

print('Higher Precision \n')
print('bBlackmanHarris : \n', bBlackmanHarris)
print('bEllip : \n', bEllip)
print('aEllip : \n', aEllip)

print('Lower Precision \n')
print('bBlackmanHarris : \n', bBlackmanHarrisArrayLowerPrecision)
print('bEllip : \n', bEllipArrayLowerPrecision)
print('aEllip : \n', aEllipArrayLowerPrecision)



fig = plt.figure(figsize=(16, 9))
plt.title("Compare Different Filters")
w, h = signal.freqz(coeffArrayHighPrecision[0][0], coeffArrayHighPrecision[0][1])
plt.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), label='Blackman-Harris High Precision')
w, h = signal.freqz(coeffArrayLowerPrecision[0][0], coeffArrayLowerPrecision[0][1])
plt.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), label='Blackman-Harris Lower Precision')
plt.xlabel('Magnitude [dB]')
plt.ylabel('Frequency [Hz]')
plt.ylim([-120, 48])
plt.xlim([20, 20000])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("FIRFilterPrecision.png")


fig = plt.figure(figsize=(16, 9))
plt.title("Compare Different Filters")
w, h = signal.freqz(coeffArrayHighPrecision[1][0], coeffArrayHighPrecision[1][1])
plt.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), label='Elliptic High Precision')
w, h = signal.freqz(coeffArrayLowerPrecision[1][0], coeffArrayLowerPrecision[1][1])
plt.semilogx((fs / 2) * (w / np.pi), 20 * np.log10(abs(h)), label='Elliptic Lower Precision')
plt.xlabel('Magnitude [dB]')
plt.ylabel('Frequency [Hz]')
plt.ylim([-120, 48])
plt.xlim([20, 20000])
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("IIRFilterPrecision.png")