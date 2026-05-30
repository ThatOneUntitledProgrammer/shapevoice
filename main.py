from src.textreader import read_text
from src.tone import load_map, build_wave, export_audio
import os


def main():
    print("ShapeVoice\n")

    files = [f for f in os.listdir("input") if f.endswith(".txt")]

    if not files:
        print("No input text found")
        return

    file_path = os.path.join("input", files[0])

    print("Reading:", files[0])
    print("Mode: Human-like triangle speech")

    text = read_text(file_path)
    freq_map = load_map()

    wave = build_wave(text, freq_map, duration=0.12)

    export_audio(wave, "output/result.wav")

    print("\n✅ Done! Check output/result.wav")


if __name__ == "__main__":
    main()