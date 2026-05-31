# ShapeVoice

ShapeVoice is not a voice AI or speech synthesis system.  

It generates synthetic audio using waveform-based methods.

---

## Features

-  Text → frequency mapping system
-  Waveform-based audio generation
-  File-based input system
-  WAV audio export
-  Experimental speech-like rhythm (not actual speech synthesis)

---

## Run ShapeVoice
```bash
git clone https://github.com/ThatOneUntitledProgrammer/shapevoice
cd shapevoice
pip install -r requirements.txt
python main.py
```

## Project Structure


![Screenshot In VSCODE](https://i.ibb.co/YF4nyzDL/Screenshot-2026-05-30-223310.png)


---

## Requirements

- Python 3.x
- numpy
- scipy

You can install dependencies using either method:

```bash
pip install numpy scipy
```
or:
```bash
pip install -r requirements.txt
```

It doesn’t matter which way, both install the same dependencies.

---

## How It Works

1. Reads text from input file  
2. Converts letters into frequency values  
3. Generates waveforms (triangle / square / noise)  
4. Builds audio signal  
5. Exports WAV file  

---

##  Project Type

- Experimental audio synthesis
- Text-to-sound engine
- Shape-based waveform generator

---

## Supported Platforms

- Windows
- Linux
- macOS

As long as Python and dependencies are installed, ShapeVoice will run on all platforms.

---

## Note

Each run overwrites `output/result.wav` by default.  
To prevent overwriting, change the output filename:

```py
export_audio(wave, "output/yourfilename.wav")
```
