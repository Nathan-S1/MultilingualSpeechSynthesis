# MultilingualSpeechSynthesis
Python project for generating multilingual speech synthesis using gTTS and other libraries.

## Author
Nathan Shorez

---

## Project Overview
This project implements a multilingual speech synthesis system using Python. The application leverages libraries such as `gTTS` to generate speech from text in various languages, with options for speed and voice selection. The objective is to provide a flexible text-to-speech system that can handle multiple languages.

---

## Key Components
- **Text-to-Speech (TTS):** Convert text into speech using `gTTS`.
- **Language Support:** Generate speech in various languages using Google Text-to-Speech.
- **Audio Output:** Save generated speech as audio files (e.g., `.mp3`).

---

## Dependencies
- Python 3.x
- gTTS
- playsound
- argparse
- os

To install dependencies:
```bash
pip install gtts playsound
```

---

## Compilation and Execution
1. **Navigate to the src directory:**
   ```bash
   cd src/
   ```
2. **Run the main script:**
   ```bash
   python speech_synthesis.py --text "Hello World" --lang "en" --output "output.mp3"
   ```

---

## Example Usage
```bash
python speech_synthesis.py --text "Hola Mundo" --lang "es" --output "spanish_output.mp3"
```

---
