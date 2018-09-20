import numpy
import matplotlib.pyplot as plot
from scipy.fftpack import fft

points = 4000
sample_rate = 48000
sampling_interval = 1/sample_rate
time_vector = numpy.linspace(0, points*sampling_interval, points)    # time from 0 to pi in 100 points
amplitude = (1,0.5,0.25,0.125)          # store amplitude as a list of values. one for each wave
frequency = (500,1000,2000,4000)           # store frequencies as a list of values. one for each wave
phase = (0,0.523599,1.0472,1.5708)
# ==================================================
# create basic waves and plot them in two sub-plots

signal_000 = amplitude[0] * numpy.sin(frequency[0]*time_vector)
signal_001 = (amplitude[0] * numpy.sin(frequency[0]*time_vector)) + \
             (amplitude[1] * numpy.sin( 10 *numpy.sin(frequency[3]*time_vector)*time_vector))

fig, axes = plot.subplots(2, 1, sharex=True, sharey=True,
                          constrained_layout=True)
axes[0].plot(time_vector,signal_000)
axes[1].plot(time_vector,signal_001)
axes[0].set_title('A Wave')
axes[1].set_title('Another Wave')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Amplitude')
plot.xlim(0,0.04)
#plot.savefig('basic_waves.png',
#    bbox_inches="tight")
plot.show()

# ==================================================
# create basic waves to compare and plot them in two sub-plots

signal_000a = amplitude[0] * numpy.sin(frequency[0]*time_vector)
signal_000b = (amplitude[0]/2) * numpy.sin(frequency[0]*time_vector)

signal_001a = amplitude[0] * numpy.sin(frequency[0]*time_vector)
signal_001b = amplitude[0] * numpy.sin(frequency[0]*2*time_vector)

signal_002a = amplitude[0] * numpy.sin(frequency[0]*time_vector + phase[0])
signal_002b = (amplitude[0]) * numpy.sin(frequency[0]*time_vector + phase[2])

fig, axes = plot.subplots(3, 1, sharex=True, sharey=True,
                          constrained_layout=True)
axes[0].plot(time_vector,signal_000a)
axes[0].plot(time_vector,signal_000b)
axes[1].plot(time_vector,signal_001a)
axes[1].plot(time_vector,signal_001b)
axes[2].plot(time_vector,signal_002a)
axes[2].plot(time_vector,signal_002b)
axes[0].set_title('Waves of different amplitudes')
axes[1].set_title('Waves of different frequencies')
axes[2].set_title('Waves with different phases')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Amplitude')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Amplitude')
plot.xlim(0,0.04)
#plot.savefig('character_waves.png',
#    bbox_inches="tight")
plot.show()

# ==================================================
# sum phases basic wave superposition

signal_000a = amplitude[0] * numpy.sin(frequency[0]*time_vector + phase[0])
signal_000b = (amplitude[0]) * numpy.sin(frequency[0]*time_vector + phase[0])
signal_000c = signal_000a + signal_000b

signal_001a = amplitude[0] * numpy.sin(frequency[0]*time_vector + phase[0])
signal_001b = (amplitude[0]) * numpy.sin(frequency[0]*time_vector + phase[3])
signal_001c = signal_001a + signal_001b

signal_002a = amplitude[0] * numpy.sin(frequency[0]*time_vector + phase[0])
signal_002b = (amplitude[0]) * numpy.sin(frequency[0]*time_vector + (phase[3]*2))
signal_002c = signal_002a + signal_002b

fig, axes = plot.subplots(3, 1, sharex=True, sharey=True,
                          constrained_layout=True)
axes[0].plot(time_vector,signal_000a,':', label='wave A')
axes[0].plot(time_vector,signal_000b,'-.', label='wave B')
axes[0].plot(time_vector,signal_000c,'-', label='result')
axes[1].plot(time_vector,signal_001a,':', label='wave A')
axes[1].plot(time_vector,signal_001b,'-.', label='wave B')
axes[1].plot(time_vector,signal_001c,'-', label='result')
axes[2].plot(time_vector,signal_002a,':', label='wave A')
axes[2].plot(time_vector,signal_002b,'-.', label='wave B')
axes[2].plot(time_vector,signal_002c,'-', label='result')
axes[0].set_title('In Phase')
axes[1].set_title('Out of Phase')
axes[2].set_title('Anti-Phase')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Amplitude')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Amplitude')
plot.legend(loc = 'best', ncol=3)
#plot.savefig('phase_sum_waves.png',
#    bbox_inches="tight")
plot.show()

# ==================================================
# sum sine waves for creating functions
signal_000_components = list()
signal_001_components = list()
signal_002_components = list()
signal_000_result = 0
signal_001_result = 0
signal_002_result = 0
for i in range(10):
    if((i%2) == 0):
        signal_001_result += (amplitude[0]/(i+1)) * \
                             numpy.sin( (frequency[0] * (i+1) ) * time_vector + phase[0])
    else:
        signal_000_result += (amplitude[0] / (i + 1)) * \
                             numpy.sin( (frequency[0] * (i + 1) ) * time_vector + phase[0])
        signal_002_result += (amplitude[0] / (i + 1)) * \
                             numpy.sin( (frequency[0] * (i+0.2) ) * time_vector + (phase[0] * (i + 1))) / 1.5
    signal_000_components.append((amplitude[0]/(i+1)) * \
                             numpy.sin( (frequency[0] * (i+1) ) * time_vector + phase[0]))
    signal_001_components.append((amplitude[0] / (i + 1)) * \
                             numpy.sin( (frequency[0] * (i + 1) ) * time_vector + phase[0]))
    signal_002_components.append((amplitude[0] / (i + 1)) * \
                             numpy.sin( (frequency[0] * (i+0.2) ) * time_vector + (phase[0] * (i + 1))) / 1.5)


fig, axes = plot.subplots(3, 1, sharex=True, sharey=True,
                          constrained_layout=True)
for i in range(10):
    if((i%2) == 0):
        axes[1].plot(time_vector, signal_001_components[i], color= 'orange', linestyle='--', alpha=0.5)
    else:
        axes[0].plot(time_vector, signal_000_components[i], color= 'orange', linestyle='--', alpha=0.5)
        axes[2].plot(time_vector, signal_002_components[i], color= 'orange', linestyle='--', alpha=0.5)
axes[0].plot(time_vector,signal_000_result)
axes[1].plot(time_vector,signal_001_result)
axes[2].plot(time_vector,signal_002_result)
axes[0].set_title('Time Domain Response: Wave 01')
axes[1].set_title('Time Domain Response: Wave 02')
axes[2].set_title('Time Domain Response: Wave 03')
axes[0].set_xlabel('Time')
axes[1].set_xlabel('Time')
axes[2].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[1].set_ylabel('Amplitude')
axes[2].set_ylabel('Amplitude')
plot.xlim(0,0.04)
#plot.savefig('sum_waves.png',
#    bbox_inches="tight")
plot.show()


freq_vector = numpy.linspace(0.0, 1.0/(2.0*sampling_interval), points//2)
# take the fft of the signal
signal_000_resultf = fft(signal_000_result)
signal_001_resultf = fft(signal_001_result)
signal_002_resultf = fft(signal_002_result)
# only half of the fft is valid
signal_000_resultf_n = 2.0/points * numpy.abs(signal_000_resultf[0:points//2])
signal_001_resultf_n = 2.0/points * numpy.abs(signal_001_resultf[0:points//2])
signal_002_resultf_n = 2.0/points * numpy.abs(signal_002_resultf[0:points//2])

fig, axes = plot.subplots(3, 1, sharex=True, sharey=True,
                          constrained_layout=True)
axes[0].semilogx(freq_vector,signal_000_resultf_n)
axes[1].semilogx(freq_vector,signal_001_resultf_n)
axes[2].semilogx(freq_vector,signal_002_resultf_n)
#axes[0].semilogx(freq_vector,20*numpy.log10(signal_000_resultf_n))
#axes[1].semilogx(freq_vector,20*numpy.log10(signal_001_resultf_n))
#axes[2].semilogx(freq_vector,20*numpy.log10(signal_002_resultf_n))
axes[0].set_title('Frequency Response: Wave 01')
axes[1].set_title('Frequency Response: Wave 02')
axes[2].set_title('Frequency Response: Wave 03')
axes[0].set_xlabel('Frequency [Hz]')
axes[1].set_xlabel('Frequency [Hz]')
axes[2].set_xlabel('Frequency [Hz]')
axes[0].set_ylabel('Amplitude')
axes[1].set_ylabel('Amplitude')
axes[2].set_ylabel('Amplitude')
plot.ylim(0,1)
plot.xlim(20,20000)
plot.savefig('fft_waves.png',
    bbox_inches="tight")
plot.show()

