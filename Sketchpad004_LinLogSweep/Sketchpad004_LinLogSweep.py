import matplotlib.pyplot
import numpy
import scipy.io.wavfile
import scipy.signal
import scipy.fftpack

lin_sample_rate, lin_signal = scipy.io.wavfile.read('LinSineSweepNew.wav','r')
log_sample_rate, log_signal = scipy.io.wavfile.read('LogSineSweepNew.wav','r')
loginv_sample_rate, loginv_signal = scipy.io.wavfile.read('LogSineSweepNewInverse.wav','r')

lin_signal = lin_signal/numpy.max(lin_signal)
log_signal = log_signal/numpy.max(log_signal)
loginv_signal = loginv_signal/numpy.max(loginv_signal)

sample_limit_plot = 1024*10
fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,5))
axes[0].set_title('Linear Sweep')
axes[0].set_xlabel('Time')
axes[0].plot(lin_signal)
axes[0].set_ylabel('Amplitude')
axes[0].set_xlim(0,sample_limit_plot)
axes[0].set_ylim(-1,1)
axes[1].set_title('Logarithmic Sweep')
axes[1].plot(log_signal)
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Amplitude')
axes[1].set_xlim(0,sample_limit_plot)
axes[1].set_ylim(-1,1)
matplotlib.pyplot.savefig('time_domainNew.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

lin_n = len(lin_signal) # length of the signal
lin_k = numpy.arange(lin_n)
lin_T = lin_n/lin_sample_rate
lin_frq = lin_k/lin_T # two sides frequency range
lin_frq = lin_frq[range(lin_n//2)] # one side frequency range
lin_Y = numpy.fft.fft(lin_signal)/lin_n # fft computing and normalization
lin_Y = lin_Y[range(lin_n//2)]

log_n = len(log_signal) # length of the signal
log_k = numpy.arange(log_n)
log_T = log_n/log_sample_rate
log_frq = log_k/log_T # two sides frequency range
log_frq = log_frq[range(log_n//2)] # one side frequency range
log_Y = numpy.fft.fft(log_signal)/log_n # fft computing and normalization
log_Y = log_Y[range(log_n//2)]

loginv_n = len(loginv_signal) # length of the signal
loginv_k = numpy.arange(loginv_n)
loginv_T = loginv_n/loginv_sample_rate
loginv_frq = loginv_k/loginv_T # two sides frequency range
loginv_frq = loginv_frq[range(loginv_n//2)] # one side frequency range
loginv_Y = numpy.fft.fft(loginv_signal)/loginv_n # fft computing and normalization
loginv_Y = loginv_Y[range(loginv_n//2)]

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,5))
axes[0].semilogx(lin_frq, 20*numpy.log10(abs(lin_Y)),'r') # plotting the spectrum
axes[0].set_title('Linear Sweep')
axes[0].set_ylabel('Frequency [Hz]')
axes[0].set_ylabel('Magnitude [dB]')
axes[0].set_xlim(20,20000)
axes[0].set_ylim(-60,-24)
axes[1].semilogx(log_frq, 20*numpy.log10(abs(log_Y)),'r') # plotting the spectrum
axes[1].set_title('Logarithmic Sweep')
axes[1].set_ylabel('Frequency [Hz]')
axes[1].set_ylabel('Magnitude [dB]')
axes[1].set_xlim(20,20000)
axes[1].set_ylim(-60,-24)
matplotlib.pyplot.savefig('frequencyDB_responseNew.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,10))
axes[0].set_title('Linear Sweep')
axes[0].specgram(lin_signal,NFFT=256,Fs=lin_sample_rate)
axes[0].set_ylim(20,20000)
axes[0].set_ylabel('Frequency [Hz]')
axes[0].set_xlabel('Time [sec]')
axes[1].set_title('Logarithmic Sweep')
axes[1].specgram(log_signal,NFFT=256,Fs=log_sample_rate)
axes[1].set_ylim(20,20000)
axes[1].set_ylabel('Frequency [Hz]')
axes[1].set_xlabel('Time [sec]')
matplotlib.pyplot.savefig('spectragramNew.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,10))
axes[0].set_title('Linear Sweep')
axes[0].specgram(lin_signal,NFFT=256,Fs=lin_sample_rate)
axes[0].set_yscale('log')
axes[0].set_ylim(20,20000)
axes[0].set_ylabel('Frequency [Hz]')
axes[0].set_xlabel('Time [sec]')
axes[1].set_title('Logarithmic Sweep')
axes[1].specgram(log_signal,NFFT=256,Fs=log_sample_rate)
axes[1].set_ylim(20,20000)
axes[1].set_yscale('log')
axes[1].set_ylabel('Frequency [Hz]')
axes[1].set_xlabel('Time [sec]')
matplotlib.pyplot.savefig('spectragramLogYNew.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,5))
axes[0].set_title('Logarithmic Sweep')
axes[0].plot(log_signal)
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[0].set_ylim(-1,1)
axes[1].set_title('Inverse Logarithmic Sweep')
axes[1].plot(loginv_signal)
axes[1].set_xlabel('Time')
axes[1].set_ylabel('Amplitude')
axes[1].set_ylim(-1,1)
matplotlib.pyplot.savefig('time_domain_compare_logs_New.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=True, sharey=True, constrained_layout=True,figsize=(10,5))
axes[0].semilogx(lin_frq, 20*numpy.log10(abs(log_Y)),'r') # plotting the spectrum
axes[0].set_title('Logarithmic Sweep')
axes[0].set_xlabel('Frequency [Hz]')
axes[0].set_ylabel('Magnitude [dB]')
axes[0].set_xlim(20,20000)
axes[0].set_ylim(-120,-24)
axes[1].semilogx(log_frq, 20*numpy.log10(abs(loginv_Y)),'r') # plotting the spectrum
axes[1].set_title('Inverse Logarithmic Sweep')
axes[1].set_xlabel('Frequency [Hz]')
axes[1].set_ylabel('Magnitude [dB]')
axes[1].set_xlim(20,20000)
axes[1].set_ylim(-120,-24)
matplotlib.pyplot.savefig('frequencyDB_response_compare_logs_New.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)

# convolve
impulse_response = scipy.signal.fftconvolve(log_signal, loginv_signal, mode='same')

IR_n = len(impulse_response) # length of the signal
IR_k = numpy.arange(IR_n)
IR_T = IR_n/loginv_sample_rate
IR_frq = IR_k/IR_T # two sides frequency range
IR_frq = IR_frq[range(IR_n//2)] # one side frequency range
IR_Y = numpy.fft.fft(impulse_response)/IR_n # fft computing and normalization
IR_Y = IR_Y[range(IR_n//2)]

fig, axes = matplotlib.pyplot.subplots(2, 1, sharex=False, sharey=False, constrained_layout=True,figsize=(10,5))
axes[0].plot(impulse_response,'r') # plotting the spectrum
axes[0].set_title('Time Domain')
axes[0].set_xlabel('Time')
axes[0].set_ylabel('Amplitude')
axes[0].set_xlim(len(impulse_response)*(0.5-0.005),len(impulse_response)*(0.5+0.005))
axes[1].semilogx(log_frq, 20*numpy.log10(abs(IR_Y)),'r') # plotting the spectrum
axes[1].set_title('Frequency Domain')
axes[1].set_xlabel('Frequency [Hz]')
axes[1].set_ylabel('Magnitude [dB]')
axes[1].set_xlim(20,20000)
axes[1].set_ylim(-120,0)
matplotlib.pyplot.savefig('response_of_IR_New.png', bbox_inches="tight")
matplotlib.pyplot.show(block=False)