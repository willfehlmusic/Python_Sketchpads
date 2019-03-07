import scipy.signal
import numpy as np
import matplotlib.pyplot as plt
import os
import imageio
import time

# system sample rate
fs = 48000
# a range of frequencies
freqRange = np.linspace(0,fs/2,fs)

# define an ideal low pass filter with cutoff at 1000 Hz
fc = 1000
# desired system frequency response
iFreqResp = []
for f in freqRange:
    if f < fc:
        iFreqResp.append(1)
    else:
        iFreqResp.append(0)

# plot frequency response of ideal low-pass filter
plt.figure(figsize=[16,9])
plt.title('Ideal Low Pass Filter:\nFrequency Response')
plt.semilogx(freqRange,iFreqResp)
plt.ylabel('Magnitude')
plt.ylim([-0.5,1.5])
plt.xlabel('Frequency [Hz]')
plt.xlim([20, 20000])
plt.grid()
plt.tight_layout()
plt.savefig('IdealFreqResponse.png', bbox_inches="tight")
#plt.show()

# use the inverse fft to create a corresponding impulse response
iTimeResp = np.fft.ifft(iFreqResp)
# only the first half of this impulse corresponds with the causal portion
iTimeResp = 2*iTimeResp[0:round(len(iTimeResp)/2)]
# create a range of time values for plotting
tRange = np.linspace(0,len(iTimeResp)-1,len(iTimeResp))

# plot the impulse response
plt.figure(figsize=[16,9])
plt.subplot(2, 1, 1)
plt.title('Ideal Low Pass Filter:\nImpulse Response')
plt.plot(tRange,iTimeResp)
plt.ylabel('Magnitude')
plt.ylim([min(iTimeResp),max(iTimeResp)])
plt.xlabel('Time [Samples]')
plt.xlim([-100, len(tRange)])
plt.grid()
plt.subplot(2, 1, 2)
plt.title('Ideal Low Pass Filter:\nImpulse Response [Zoomed]')
plt.plot(tRange,iTimeResp)
plt.ylabel('Magnitude')
plt.ylim([min(iTimeResp),max(iTimeResp)])
plt.xlabel('Time [Samples]')
plt.xlim([0, 512])
plt.grid()
plt.tight_layout()
plt.savefig('IdealTimeResponse.png', bbox_inches="tight")
#plt.show()

# hard truncate the impulse response to an acceptable number of coefficients
nCoeff = 2048
iTimeRespTrunc = np.concatenate([iTimeResp[0:nCoeff],
                                np.zeros(len(iTimeResp) - nCoeff)])
# get the frequency response
iFreqResp = np.fft.fft(iTimeRespTrunc,len(iTimeRespTrunc))
# a range of frequencies
freqRange = np.linspace(0,fs/2,len(iTimeRespTrunc))

# plot the impulse and frequency response
plt.figure(figsize=[16,9])
plt.subplot(2, 1, 1)
plt.title('Impulse Response [Truncated]')
plt.plot(tRange,iTimeRespTrunc)
plt.ylabel('Magnitude')
plt.ylim([min(iTimeRespTrunc),max(iTimeRespTrunc)])
plt.xlabel('Time [Samples]')
plt.xlim([0, len(tRange[0:nCoeff])])
plt.grid()
plt.subplot(2, 1, 2)
plt.title('Frequency Response [Truncated]')
plt.semilogx(freqRange,np.real(iFreqResp))
plt.ylabel('Magnitude')
plt.ylim([-0.5,1.5])
plt.xlabel('Frequency [Hz]')
plt.xlim([20, 20000])
plt.grid()
plt.tight_layout()
plt.savefig('TruncatedResponse.png', bbox_inches="tight")
#plt.show()

# setting up to export images...
# set up figure
fig = plt.figure(figsize=[16,9])
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.set_ylabel('Magnitude')
ax1.set_ylim([min(iTimeResp),max(iTimeResp)])
ax1.set_xlabel('Time [Samples]')

ax2.set_ylabel('Magnitude')
ax2.set_xlabel('Frequency [Hz]')
ax2.set_ylim([-0.5,1.5])
ax2.set_xlim([20, 20000])
#plt.show(block=False)
count = 0
for n in range(512, 8, -4):
    # print(n)
    # clear the plots
    ax1.cla()
    ax2.cla()
    # adjust plot titles
    ax1.set_title('Impulse Response: samples={}'.format(n))
    ax2.set_title('Frequency Response n={}'.format(n))
    # replotting for a new number of coefficients
    nCoeff = n
    iTimeRespTrunc = np.concatenate([iTimeResp[0:nCoeff],
                                    np.zeros(len(iTimeResp) - nCoeff)])
    # adjust data
    iFreqResp = np.fft.fft(iTimeRespTrunc,len(iTimeRespTrunc))
    # a range of frequencies
    freqRange = np.linspace(0,fs/2,len(iTimeRespTrunc))
    # plot the data
    ax1.plot(tRange, iTimeRespTrunc)
    ax2.semilogx(freqRange,np.real(iFreqResp))
    # re-adjust the range
    ax1.set_xlim([0, n])
    ax2.set_ylim([-0.5,1.5])
    ax2.set_xlim([20,20000])
    ax1.grid(True)
    ax2.grid(True)
    a = str(count).zfill(8)
    # save files
    plt.savefig('Frames/TruncatedResponse_'+a+'.png', bbox_inches="tight")
    count += 1


# make gif out of each image file
png_dir = 'Frames/'
images = []
for file_name in os.listdir(png_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(png_dir, file_name)
        images.append(imageio.imread(file_path))
imageio.mimsave('TruncationAnimation.gif', images)

# convert .gif to .mp4
import moviepy.editor as mp
clip = mp.VideoFileClip("TruncationAnimation.gif")
clip.write_videofile("TruncationAnimation.mp4")
# FIR Filter Design: The Effect of Impulse Response Truncation on my YouTube

# now lets really do the truncation
# Hard truncate the impulse response to an acceptable number of coefficients
nCoeff = 64
iTimeRespTrunc = np.concatenate([iTimeResp[0:nCoeff],
                                np.zeros(len(iTimeResp) - nCoeff)])
# frequency response
iFreqResp = np.fft.fft(iTimeRespTrunc,len(iTimeRespTrunc))
# a range of frequencies
freqRange = np.linspace(0,fs/2,len(iTimeRespTrunc))

plt.figure(figsize=[16,9])
plt.subplot(2, 1, 1)
plt.title('Impulse Response [Truncated]')
plt.plot(tRange,iTimeRespTrunc)
plt.ylabel('Magnitude')
plt.ylim([min(iTimeRespTrunc),max(iTimeRespTrunc)])
plt.xlabel('Time [Samples]')
plt.xlim([0, len(tRange[0:nCoeff])])
plt.grid()
plt.subplot(2, 1, 2)
plt.title('Frequency Response [Truncated]')
plt.semilogx(freqRange,np.real(iFreqResp))
plt.ylabel('Magnitude')
plt.ylim([-0.5,1.5])
plt.xlabel('Frequency [Hz]')
plt.xlim([20, 20000])
plt.grid()
plt.tight_layout()
plt.savefig('TruncatedResponse_64Coefficient.png', bbox_inches="tight")

nCoeff = 128
# compare windowing functions use 128+ samples for acceptable frequency graph
negposTRange = np.linspace(-nCoeff,nCoeff,nCoeff*2)
boxcar_window = scipy.signal.windows.boxcar(nCoeff*2)
boxcar_window[0] = 0
boxcar_window[len(boxcar_window)-1] = 0
triang_window = scipy.signal.windows.triang(nCoeff*2)
exponential_window = scipy.signal.windows.exponential(nCoeff*2)
cosine_window = scipy.signal.windows.cosine(nCoeff*2)
blackmanharris_window = scipy.signal.windows.blackmanharris(nCoeff*2)
hamming_window = scipy.signal.windows.hamming(nCoeff*2)

# this function just gets the frequency response and frequency range for each window...
# make life easier
def getFreqResponse(window):
    A = np.fft.fft(window, len(window)) / 25.5
    mag = np.abs(np.fft.fftshift(A))
    freq = np.linspace(-0.5, 0.5, len(A))
    response = 20.0 * np.log10(np.real(mag))
    response = np.clip(response, -120, 120)
    return freq, response
boxcar_windowResponse = getFreqResponse(boxcar_window)
triang_windowResponse = getFreqResponse(triang_window)
exponential_windowResponse = getFreqResponse(exponential_window)
cosine_windowResponse = getFreqResponse(cosine_window)
blackmanharris_windowResponse = getFreqResponse(blackmanharris_window)
hamming_windowResponse = getFreqResponse(hamming_window)

# plot time domain response and frequency response
plt.figure(figsize=[16,10])
plt.subplot(3, 2, 1)
plt.plot(negposTRange, boxcar_window)
plt.title("Boxcar Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 2)
plt.plot(boxcar_windowResponse[0], boxcar_windowResponse[1])
plt.title("Boxcar Window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()

plt.subplot(3, 2, 3)
plt.plot(negposTRange, triang_window)
plt.title("Triangle Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 4)
plt.plot(triang_windowResponse[0], triang_windowResponse[1])
plt.title("Triangle window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()

plt.subplot(3, 2, 5)
plt.plot(negposTRange, exponential_window)
plt.title("Exponential Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 6)
plt.plot(exponential_windowResponse[0], exponential_windowResponse[1])
plt.title("Exponential window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()

plt.savefig('WindowResponse_128Coefficient_set1.png', bbox_inches="tight")


plt.figure(figsize=[16,10])
plt.subplot(3, 2, 1)
plt.plot(negposTRange, cosine_window)
plt.title("Cosine Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 2)
plt.plot(cosine_windowResponse[0], cosine_windowResponse[1])
plt.title("Cosine window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()


plt.subplot(3, 2, 3)
plt.plot(negposTRange, blackmanharris_window)
plt.title("Blackman-Harris Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 4)
plt.plot(blackmanharris_windowResponse[0], blackmanharris_windowResponse[1])
plt.title("Blackman-Harris window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()

plt.subplot(3, 2, 5)
plt.plot(negposTRange, hamming_window)
plt.title("Hamming Window")
plt.ylabel("Amplitude")
plt.ylim([0,1.1])
plt.xlabel("Time [samples]")
plt.grid()
plt.subplot(3, 2, 6)
plt.plot(hamming_windowResponse[0], hamming_windowResponse[1])
plt.title("Hamming window")
plt.ylabel("Amplitude [dB]")
plt.xlabel("Frequency [normalized]")
plt.grid()
plt.tight_layout()

plt.savefig('WindowResponse_128Coefficient_set2.png', bbox_inches="tight")


# okay so now back to our truncated  impulse response...
# let's do truncation and apply the windowing function...
nCoeff = 64
# make double wide window...
boxcar_window = scipy.signal.windows.boxcar(nCoeff*2)
triang_window = scipy.signal.windows.triang(nCoeff*2)
cosine_window = scipy.signal.windows.cosine(nCoeff*2)
blackmanharris_window = scipy.signal.windows.blackmanharris(nCoeff*2)
hamming_window = scipy.signal.windows.hamming(nCoeff*2)
# take only the positive portion of the window and...
# make the array the same length as the impulse response
iTimeRespTrunc = np.concatenate([iTimeResp[0:nCoeff],
                                np.zeros(len(iTimeResp) - nCoeff)])
boxcar_window = np.concatenate([boxcar_window[nCoeff:],
                                 np.zeros(len(iTimeRespTrunc) - nCoeff)])
boxcar_window = boxcar_window * iTimeRespTrunc

triang_window = np.concatenate([triang_window[nCoeff:],
                                 np.zeros(len(iTimeRespTrunc) - nCoeff)])
triang_window = triang_window * iTimeRespTrunc

cosine_window = np.concatenate([cosine_window[nCoeff:],
                                 np.zeros(len(iTimeRespTrunc) - nCoeff)])
cosine_window = cosine_window * iTimeRespTrunc

blackmanharris_window = np.concatenate([blackmanharris_window[nCoeff:],
                                 np.zeros(len(iTimeRespTrunc) - nCoeff)])
blackmanharris_window = blackmanharris_window * iTimeRespTrunc

hamming_window = np.concatenate([hamming_window[nCoeff:],
                                 np.zeros(len(iTimeRespTrunc) - nCoeff)])
hamming_window = hamming_window * iTimeRespTrunc

# get frequency response of windowed responses...
iFreqResp_boxcar = np.fft.fft(np.real(boxcar_window),len(boxcar_window))
iFreqResp_triang = np.fft.fft(np.real(triang_window),len(triang_window))
iFreqResp_cosine = np.fft.fft(np.real(cosine_window),len(cosine_window))
iFreqResp_blackmanharris = np.fft.fft(np.real(blackmanharris_window),len(blackmanharris_window))
iFreqResp_hamming = np.fft.fft(np.real(hamming_window),len(hamming_window))
# a range of frequencies
freqRange = np.linspace(0,fs/2,len(hamming_window))

plt.figure(figsize=[16,9])
plt.subplot(2, 1, 1)
plt.title('Impulse Response [Truncated]')
plt.plot(tRange,np.real(boxcar_window), label='boxcar')
plt.plot(tRange,np.real(triang_window), label='triangle')
plt.plot(tRange,np.real(cosine_window), label='cosine')
plt.plot(tRange,np.real(blackmanharris_window), label='blackman-harris')
plt.plot(tRange,np.real(hamming_window), label='hamming')
plt.ylabel('Magnitude')
plt.ylim([min(boxcar_window),max(boxcar_window)])
plt.xlabel('Time [Samples]')
plt.xlim([0, len(tRange[0:nCoeff])])
plt.legend()
plt.grid()
plt.subplot(2, 1, 2)
plt.title('Frequency Response [Truncated]')
plt.semilogx(freqRange,iFreqResp_boxcar, label='boxcar')
plt.semilogx(freqRange,iFreqResp_triang, label='triangle')
plt.semilogx(freqRange,iFreqResp_cosine, label='cosine')
plt.semilogx(freqRange,iFreqResp_blackmanharris, label='blackman-harris')
plt.semilogx(freqRange,iFreqResp_hamming, label='hamming')
plt.ylabel('Magnitude')
#plt.ylim([-0.5,1.5])
plt.xlabel('Frequency [Hz]')
plt.xlim([20, 20000])
plt.grid()
plt.tight_layout()
plt.savefig('FilterWindows_64Coefficient.png', bbox_inches="tight")

# print coefficients...
print('boxcar \t', np.real(boxcar_window[0:nCoeff]) )
print('triangle \t', np.real(triang_window[0:nCoeff]) )
print('cosine \t', np.real(cosine_window[0:nCoeff]) )
print('blackman-harris \t', np.real(blackmanharris_window[0:nCoeff]) )
print('hamming_window \t', np.real(hamming_window[0:nCoeff]) )