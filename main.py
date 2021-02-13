import sys
import os

import speech_recognition as sr

#URL of the google drive folder

#URL = sys.argv[0]


from moviepy.editor import *

path = r"C:\Users\sunee\Desktop\Workspace\Oh_My_Video"

#####print(os.path,"\n")

# video = VideoFileClip(os.path.join(path,path,"Feb_12.mp4"))
# # video.audio.write_audiofile(os.path.join(path,path,"Feb_12_sound.mp3"))
# video.audio.write_audiofile(os.path.join(path,path,"test.wav"),codec='pcm_s16le')


from pydub import AudioSegment

# # files                                                                         
# src = os.path.join(path,path,"Feb_12_sound.mp3")
dst = os.path.join(path,path,"test.wav")



# # convert wav to mp3    

# ###print(src,"\n",dst)

# sound = AudioSegment.from_mp3(src)
# sound.export(dst, format="wav")
t1 = 600
t2 = 650
t1 = t1 * 1000 #Works in milliseconds
t2 = t2 * 1000
# newAudio = AudioSegment.from_wav(dst)
# newAudio = newAudio[t1:t2]
# newAudio.export(os.path.join(path,path,"test_excerpt.wav"), format="wav")

final_path = os.path.join(path,path,"test_excerpt.wav")

r = sr.Recognizer()
audio = sr.AudioFile(final_path)

with audio as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source,duration = 50)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)#, language = "fr-FR")
    print(text)









# # command2mp3 = “ffmpeg -i Feb_12.mp4 Feb_12.mp3”
# # command2wav = “ffmpeg -i Feb_12.mp3 Feb_12.wav”

# # os.system(command2mp3)
# #os.system(command2wav)