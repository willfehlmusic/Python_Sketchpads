import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
from matplotlib import patches
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.figure import Figure
from matplotlib import rcParams

def zplot(b=[-0.2, 0.3, 0.1], a = [1]):
    """
    Plot the complex z-plane given a filters coefficients.
    - give plot as a surface
    """

    # create the mesh in polar coordinates and compute corresponding Z.
    radiusArray = np.linspace(0, 1, 64)
    freqArray = np.linspace(0, 2 * np.pi, 128)

    magnitudeArrayMesh, phaseangleArrayMesh = np.meshgrid(radiusArray, freqArray)
    # print("radiusArrayMesh ", radiusArrayMesh)
    # print("freqArrayMesh ", freqArrayMesh)
    coordinateX = magnitudeArrayMesh * np.cos(phaseangleArrayMesh)
    coordinateY = magnitudeArrayMesh * np.sin(phaseangleArrayMesh)
    # print("coordinateX ", coordinateX)
    # print("coordinateY ", coordinateY)

    Z = magnitudeArrayMesh * (np.e ** (1j * phaseangleArrayMesh))
    # print("Z ", Z)
    Bejw = 0 + 0j
    for index in range(len(b)):
        Bejw += b[index] * (Z ** -index)
    Aejw = 0 + 0j
    for index in range(len(a)):
        Aejw -= a[index] * (Z ** -index)

    H_z = Bejw/Aejw
    # print("H_z ", H_z)
    H_z_real = np.real(H_z)
    H_z_imag = np.imag(H_z)
    #print("H_z_real ", H_z_real)
    #print("H_z_imag ", H_z_imag)
    FreqZ = []
    Z_dB = 20 * np.log10(np.sqrt((H_z_real ** 2) + (H_z_imag ** 2)))
    for row in Z_dB:
        FreqZ.append(row[len(row) - 1])
    #print("Z_dB ", Z_dB)

    # Plot the 3D surface
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(coordinateX, coordinateY, Z_dB, rstride=1, cstride=1, alpha=0.8, cmap='brg', vmin=-60.,
                           vmax=60.)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=10)
    # Customize the z axis.
    ax.view_init(45, -120)
    ax.set_zlim(-60, 12)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Magnitude [dB]")
    plt.savefig('ZSurfaceSide.png')

    # Plot the 3D surface
    fig = plt.figure(figsize=(16, 10))
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_surface(coordinateX, coordinateY, Z_dB, rstride=1, cstride=1, alpha=0.8, cmap='brg', vmin=-24.,
                           vmax=24.)
    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=10)
    # Customize the z axis.
    ax.view_init(90, -90)
    ax.set_zlim(-60, 12)
    ax.set_ylim([-1, 1])
    ax.set_xlim([-1, 1])
    ax.zaxis.set_major_locator(LinearLocator(9))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.set_xlabel("Real")
    ax.set_ylabel("Imaginary")
    ax.set_zlabel("Magnitude [dB]")
    plt.savefig('ZSurfaceTop.png')

    fig, ax1 = plt.subplots()
    ax1.set_title('Digital filter frequency response')
    ax1.plot(freqArray, FreqZ, 'b')
    ax1.set_ylabel('Amplitude [dB]')
    ax1.set_ylim([-60, 24])
    ax1.set_xlabel('Frequency [rad/sample]')
    ax1.set_xlim([0, (np.pi)])
    plt.savefig('ZFreq.png')
    plt.grid()

    return

z, p, k = scipy.signal.iirfilter(3, 0.5, rp=6, rs=54, btype='lowpass', ftype='ellip', output='zpk')
print('zeros : \n', z)
print('poles : \n', p)

bEllip, aEllip = scipy.signal.iirfilter(3, 0.5, rp=6, rs=54, btype='lowpass', ftype='ellip')
bt = bEllip#[0.6, -0.5, 0.1, -0.2, 0.3]#bEllip
at = aEllip#[0.2, -0.1, -0.0005, 0.2, -0.0002]#aEllip#[1]
print("b Coefficients :\n", bt)
print("a Coefficients :\n", at)
zplot(bt,at)

inputSignal = np.zeros(128)
inputSignal[0] = 1

fig = plt.figure(figsize=(16, 10))
fImpulse = scipy.signal.lfilter(b=bt, a=at,x=inputSignal)  # calculate impulse response
plt.plot(fImpulse)
plt.xlabel('Time [samples]')
plt.xlim([0, 128])
plt.ylabel('Amplitude')
plt.grid(which='both', axis='both')
plt.savefig('TimeDomainResponse.png')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

