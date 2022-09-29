# from playsound import playsound 
# playsound('s.mp3')


# from gtts import gTTS
# from io import BytesIO
# # mp3_fp = BytesIO()
# # tts = gTTS('hello', lang='en')
# # tts.write_to_fp(mp3_fp)

# from gtts import gTTS
# from tempfile import TemporaryFile
# import tempfile
# tts = gTTS(text='Hello', lang='en')
# f = tempfile.TemporaryFile(suffix="wav")
# tts.write_to_fp(f)
# playsound(f)
# f.close()
# _*_ coding: utf-8 _*_
#! /usr/bin/python

# import time
# from gtts import gTTS
# from tempfile import TemporaryFile
# from IPython.display import Audio

# tts = gTTS(text='Dataset successfully imported', lang='en')
# f = TemporaryFile()
# tts.write_to_fp(f)
# f.seek(0)
# Audio(f.read(), autoplay=True)
# time.sleep(5) # doesn't work to avoid the file to close to fast...
# f.close() # ... this has to be in the next cell otherwise the sound is not played
import pyttsx3

f = pyttsx3.init()
ans = input("hello world:")
f.say(ans)
f.runAndWait()






