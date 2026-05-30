import json
import numpy as np
from scipy.io.wavfile import write

from src.shapes.triangle import triangle_wave

SR = 44100


def load_map():
    with open("src/list/hz_by_letter.json", "r") as f:
        return json.load(f)


# 🎤 smoother "voice envelope" (IMPORTANT)
def apply_envelope(wave):
    fade = int(len(wave) * 0.1)

    envelope = np.ones(len(wave))
    envelope[:fade] = np.linspace(0, 1, fade)
    envelope[-fade:] = np.linspace(1, 0, fade)

    return wave * envelope


# 🧠 HUMAN-LIKE SPEECH BUILDER
def build_wave(text, freq_map, duration=0.12):
    audio = []

    words = text.upper().split(" ")

    for word in words:

        for letter in word:

            if letter not in freq_map:
                continue

            freq = freq_map[letter]

            # triangle = soft voice base
            wave = triangle_wave(freq, duration)

            # smoother transitions (key for “human feel”)
            wave = apply_envelope(wave)

            audio.extend(wave)

        # 🫁 word pause (breathing space)
        audio.extend(np.zeros(int(SR * duration * 2)))

    return np.array(audio)


def export_audio(wave, output_path):
    wave = wave / np.max(np.abs(wave))
    wave = (wave * 32767).astype(np.int16)

    write(output_path, SR, wave)