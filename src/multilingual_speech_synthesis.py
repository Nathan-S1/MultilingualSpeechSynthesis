# -*- coding: utf-8 -*-
"""Multilingual Speech Synthesis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/108itKtT-BP5DrsWoG_YT0qe2W5s8Jla-
"""

!pip install gradio
!pip install git+https://github.com/openai/whisper.git
!pip install translate
!pip install TTS
!pip install ffmpeg

import gradio as gr
import whisper
from translate import translate
from TTS.api import TTS
import ffmpeg

model = whisper.load_model("large-v2")

def speech_to_text(audio):
    result = model.transcribe(audio)
    return result["text"]

def translate(text, language):
    translator = Translator(to_lang=language)
    translated_text = translator.translate(text)
    return translated_text

tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu = False)

def s2s(audio, language):
  result_text = speech_to_text(audio)
  translated_text = translate(result_text, language)
  tts_model.tts_to_file(text=translated_text, file_path="output.wav", speaker_wav=audio, language = language)

  with open("output.wav", "rb") as file:
    audio_data = file.read()

  return [result_text, translated_text, audio_data]

language_names = ["Chinese", "French", "German", "Russian", "Spanish"]
language_options = ["zn-cn", "fr", "de", "ru", "es"]

language_dropdown = gr.Dropdown(choices = zip(language_names, language_options), value= "es", label="Target Language",)

translate_button = gr.Button(value="Synthesize and Translate my Voice!")
transcribed_text = gr.Textbox(label="Transcribed Text")
output_text = gr.Textbox(label="Translated Text")
output_speech = gr.Audio(label="Translated Speech", type="filepath")

demo = gr.Interface(
    fn=s2s,
    inputs=[gr.Audio(sources=["upload", "microphone"], type="filepath", format = "wav",show_download_button=True), language_dropdown],
    outputs=[transcribed_text, output_text, output_speech],

    title="Speech-to-Speech Translation - Nathan Shorez"
)
demo.launch(debug=True, share = True)