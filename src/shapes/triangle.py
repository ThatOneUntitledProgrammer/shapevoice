import numpy as np

def triangle_wave(freq, duration, sr=44100):
    t = np.linspace(0, duration, int(sr * duration), False)
    return 2 * np.abs(2 * ((t * freq) % 1) - 1) - 1