import numpy as np

'''
This script is only meant to show what happens when you map a complex value z
to a Cartesian grid. This corresponds with the article on my LinkedIn:

'''

# basic parameters
sampleFrequency = 48000
nyquist = sampleFrequency/2
# I wish to display these points
f = [nyquist/4, nyquist/2, nyquist, 3*sampleFrequency/4, sampleFrequency]

# create an empty list to hold various values of omega
omega = []
for i in f:
    omega.append(2 * np.pi * (i/sampleFrequency))
# n samples time
timeSamples = np.linspace(0,sampleFrequency,sampleFrequency+1)
# I want to investigate these values of A
gainFactor = [0.75,1,1.05]

# Let us use cosine + sine form to create complex numbers.
# make the unit circle
zunitcicle = 1*(np.cos(np.linspace(0,2*np.pi,sampleFrequency)) + 1j*np.sin(np.linspace(0,2*np.pi,sampleFrequency)))
#this is for the first set of graphs
zAT0 = gainFactor[0]*(np.cos(omega) + 1j*np.sin(omega))
fxR0 = pow(gainFactor[0],-1*timeSamples)*(np.cos(omega[0]*timeSamples))
fxI0 = pow(gainFactor[0],-1*timeSamples)*(np.sin(omega[0]*timeSamples))

#this is for the second set of graphs
zAT1 = gainFactor[1]*(np.cos(omega) + 1j*np.sin(omega))
fxR1 = pow(gainFactor[1],-1*timeSamples)*(np.cos(omega[0]*timeSamples))
fxI1 = pow(gainFactor[1],-1*timeSamples)*(np.sin(omega[0]*timeSamples))

#this is for the third set of graphs
zAT2 = gainFactor[2]*(np.cos(omega) + 1j*np.sin(omega))
fxR2 = pow(gainFactor[2],-1*timeSamples)*(np.cos(omega[0]*timeSamples))
fxI2 = pow(gainFactor[2],-1*timeSamples)*(np.sin(omega[0]*timeSamples))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(timeSamples[1:100],fxR0[1:100])
plt.title("Real\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-10,10)
plt.grid()
plt.subplot(2,2,2)
plt.plot(timeSamples[1:100],fxI0[1:100])
plt.title("Imaginary\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-10,10)
plt.grid()
plt.subplot(2,2,3)
plt.title('A = {}'.format(gainFactor[0]))
plt.scatter(zAT0.real,zAT0.imag)
plt.plot(zunitcicle.real,zunitcicle.imag,'g')
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.axis('equal')
plt.axis([-2, 2, -2, 2])
plt.grid()
plt.savefig('ZPlotUnstable.png',
    bbox_inches="tight")

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(timeSamples[1:100],fxR1[1:100])
plt.title("Real\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-2,2)
plt.grid()
plt.subplot(2,2,2)
plt.plot(timeSamples[1:100],fxI1[1:100])
plt.title("Imaginary\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-2,2)
plt.grid()
plt.subplot(2,2,3)
plt.title('A = {}'.format(gainFactor[1]))
plt.scatter(zAT1.real,zAT1.imag)
plt.plot(zunitcicle.real,zunitcicle.imag,'g')
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.axis('equal')
plt.axis([-2, 2, -2, 2])
plt.grid()
plt.savefig('ZPlotSteady.png',
    bbox_inches="tight")

plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.plot(timeSamples[1:100],fxR2[1:100])
plt.title("Real\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-2,2)
plt.grid()
plt.subplot(2,2,2)
plt.plot(timeSamples[1:100],fxI2[1:100])
plt.title("Imaginary\n Freq = fs/4 kHz")
plt.xlabel("Time [samples]")
plt.ylabel("Amplitude")
plt.ylim(-2,2)
plt.grid()
plt.subplot(2,2,3)
plt.title('A = {}'.format(gainFactor[2]))
plt.scatter(zAT2.real,zAT2.imag)
plt.plot(zunitcicle.real,zunitcicle.imag,'g')
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.axis('equal')
plt.axis([-2, 2, -2, 2])
plt.grid()
plt.savefig('ZPlotStable.png',
    bbox_inches="tight")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
plt.figure(figsize=(10,10))
plt.title('A = {}'.format(gainFactor[1]))
plt.scatter(zAT1.real,zAT1.imag)
plt.plot(zunitcicle.real,zunitcicle.imag,'g')
plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.axis('equal')
plt.axis([-2, 2, -2, 2])
plt.grid()
plt.savefig('ZPlotStableCircle.png',
    bbox_inches="tight")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
