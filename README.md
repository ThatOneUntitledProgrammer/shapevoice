# ShapeVoice

ShapeVoice is an experimental text-to-sound engine. It is not a voice AI or text-to-speech system.

It generates WAV files from text using frequency mapping and procedural sound waves.

---

## Features

-  Text → frequency mapping system
-  Waveform-based audio generation
-  File-based input system
-  WAV audio export
-  Human-like speech rhythm (experimental and not might not be accurate)

---

## Project Structure


![Screenshot In VSCODE](https://i.ibb.co/YF4nyzDL/Screenshot-2026-05-30-223310.png)


---

## Requirements

- Python 3.x
- numpy
- scipy

Install dependencies:

```bash
pip install numpy scipy
```

---

##  How to Run

1. Add your text inside:
```
input/example.txt
```

2. Run the program:

```bash
python main.py
```

3. Output audio will be saved as:
```
output/result.wav
```

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

1. ShapeVoice is not a real human speech engine.  
It is a **procedural waveform synthesis (experimental)** designed for experimentation and audio generation,
ShapeVoice does not generate real human speech. 
2. Any files you make. it overwrites the old result.wav so before running if you want. please change :
```py
export_audio(wave, "output/result.wav")
```
to:
```py
export_audio(wave, "output/yourfilename.wav")
```
