import numpy as np
import matplotlib.pyplot as plt

# Step 1: Generate a Gaussian random field
np.random.seed(42)  # For reproducibility
x = np.linspace(0, 10, 1000)  # 1D spatial domain
original_signal = np.sin(x)

# Step 2: Apply Fourier transform
ft = np.fft.fft(original_signal)
k = np.fft.fftfreq(len(x), d=(x[1] - x[0]))

# Randomize the phases
random_phases = np.exp(1j * 2 * np.pi * np.random.random(len(ft)))
randomized_ft = np.abs(ft) * random_phases

# Inverse Fourier transform to get the randomized signal
randomized_signal = np.fft.ifft(randomized_ft).real

# Compute power spectrum
power_spectrum_original = np.abs(ft) ** 2
power_spectrum_randomized = np.abs(randomized_ft) ** 2

# Step 3: Plot the results
plt.figure(figsize=(15, 5))

# Plot original and randomized signals
plt.subplot(1, 3, 1)
plt.plot(x, original_signal, label="Original Signal", color="blue")
plt.title("Original Signal")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid()

plt.subplot(1, 3, 2)
plt.plot(x, randomized_signal, label="Randomized Signal", color="red")
plt.title("Randomized Signal")
plt.xlabel("x")
plt.ylabel("Amplitude")
plt.grid()

# Plot power spectrum
plt.subplot(1, 3, 3)
k_positive = k[k>=0]
power_spectrum_original_positive = power_spectrum_original[k >= 0]
power_spectrum_randomized_positive = power_spectrum_randomized[k >= 0]
plt.plot(k_positive, power_spectrum_original_positive, label="Original", color="blue")
plt.plot(k_positive, power_spectrum_randomized_positive, label="Randomized", color="red", linestyle="dashed")
#plt.xlim(-1, 1)
plt.title("Power Spectrum")
plt.xlabel("Wave number (k)")
plt.ylabel("Power")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

print("Hello World")
print("new lines in the python branch")

print("another new line in the python branch")
