import numpy as np
import soundfile as sf
import yaml

import tensorflow as tf

from tensorflow_tts.inference import TFAutoModel
from tensorflow_tts.inference import AutoProcessor
import gradio as gr

# initialize fastspeech2 model.
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")


# initialize mb_melgan model
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")


# inference
processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-ljspeech-en")

def inference(text):
  input_ids = processor.text_to_sequence(text)
  # fastspeech inference
  
  mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
      input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
      speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
      speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
      f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
      energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
  )

  # melgan inference
  audio_before = mb_melgan.inference(mel_before)[0, :, 0]
  audio_after = mb_melgan.inference(mel_after)[0, :, 0]
  
  # save to file
  sf.write('./audio_before.wav', audio_before, 22050, "PCM_16")
  sf.write('./audio_after.wav', audio_after, 22050, "PCM_16")
  return './audio_after.wav'
  
inputs = gr.inputs.Textbox(lines=5, label="Input Text")
outputs =  gr.outputs.Audio(type="file", label="Output Audio")


title = "Tensorflow TTS"
description = "Gradio demo for TensorFlowTTS: Real-Time State-of-the-art Speech Synthesis for Tensorflow 2. To use it, simply add your text, or click one of the examples to load them."
article = "<p style='text-align: center'><a href='https://ruslanmv.com/'> Check out more Machine Learning projects at my blog </a> | <a href='https://github.com/ruslanmv/TensorFlowTTS'>Github Repo</a></p>"

examples = [
 ["TensorFlowTTS provides real-time state-of-the-art speech synthesis architectures such as Tacotron-2, Melgan, Multiband-Melgan, FastSpeech, FastSpeech2 based-on TensorFlow 2."],
 ["With Tensorflow 2, we can speed-up training/inference progress, optimizer further by using fake-quantize aware and pruning, make TTS models can be run faster than real-time and be able to deploy on mobile devices or embedded systems."]   
]

gr.Interface(inference, inputs, outputs, title=title, description=description, article=article, examples=examples).launch()