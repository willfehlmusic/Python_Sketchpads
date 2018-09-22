import numpy
import matplotlib.pyplot

# define properties of wave
amplitude = 1
frequency = 500
phase_in_degrees = 0
# convert phase in to radians
phase_in_radians = phase_in_degrees * (180/numpy.pi)

# define time vector
points = 400
sample_rate = 48000
sampling_interval = 1/sample_rate
time_vector_00 = numpy.linspace(0, points*sampling_interval, points)
# define bit-depth
n_bits = 2
quantization_stepsize = 1/numpy.power(2, n_bits)


def signal(arg_amplitude, arg_frequency, arg_phase, arg_time_vector):
    # create a signal
    signal = arg_amplitude * numpy.sin( 2 * numpy.pi * arg_frequency * \
                                        arg_time_vector + arg_phase)
    # return the signal
    return signal

def quantize(arg_signal, arg_quantization_stepsize = 1/4):
    # copy the signal
    signal=numpy.copy(arg_signal)
    # if the signal is >= 1 then limit the signal
    index_signal = numpy.where(numpy.abs(signal) >= 1)
    # rewrite the signal with each element of correct polarity
    signal[index_signal] = numpy.sign(signal[index_signal])
    # quantize the signal
    quantized_signal = arg_quantization_stepsize * \
                       numpy.floor(signal/arg_quantization_stepsize + \
                                   0.5)
    # return the quantized signal
    return quantized_signal

def error(arg_signal, arg_quantized_signal):
    # the error signal is defined as the differences between the two signals
    error_signal = arg_quantized_signal - arg_signal
    # return the error signal
    return error_signal

def sampled_signal(arg_signal, arg_step):
    # arg_step is the integer factor to down-sample by
    # copy the signal
    signal=numpy.copy(arg_signal)
    index_to_use = arg_step
    for i in range(len(signal)):
        if i == index_to_use:
            # increment the value
            index_to_use += arg_step
        else:
            # zero the value
            signal[i] = 0
    return signal

# call functions
signal_01_a = signal(amplitude,frequency,phase_in_degrees,time_vector_00)
signal_01_q = quantize(signal_01_a, quantization_stepsize)
signal_01_e = error(signal_01_a, signal_01_q)
signal_01_b = sampled_signal(signal_01_a, 4)

# plot signals for sample rate demo
matplotlib.pyplot.figure(figsize=(10,5))
matplotlib.pyplot.plot(signal_01_a, label='Original Signal')
matplotlib.pyplot.stem(signal_01_b, label='12 kHz Sample Rate')
matplotlib.pyplot.xlabel('time')
matplotlib.pyplot.xlim(0,points/4)
matplotlib.pyplot.title('Sampled 500 Hz Wave')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid()
matplotlib.pyplot.savefig('sampling.png', bbox_inches="tight")
matplotlib.pyplot.show()

# plot signals for quantization demo
matplotlib.pyplot.figure(figsize=(10,5))
matplotlib.pyplot.plot(signal_01_a, ':' ,label='discrete signal')
matplotlib.pyplot.plot(signal_01_q, label='quantized signal')
matplotlib.pyplot.plot(signal_01_e, label='quantization error')
matplotlib.pyplot.xlabel('time')
matplotlib.pyplot.xlim(0,points/2)
matplotlib.pyplot.title('2 Bit Quantization')
matplotlib.pyplot.legend()
matplotlib.pyplot.grid()
matplotlib.pyplot.savefig('quantization.png', bbox_inches="tight")
matplotlib.pyplot.show()