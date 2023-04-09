from pydub import AudioSegment
import wave
import pylab as pl
ff_path = 'D:/downloads/ffmpeg-2023-04-06-git-b564ad8eac-essentials_build/bin/ffmpeg.exe'
AudioSegment.converter = ff_path
song = AudioSegment.from_file(r'D:\part_job\Real_Time_Speech_Emotion_Recognition\Data\changed_m4a\clam.m4a')#路径可以使用绝对路径也可以使用相对路径
song.export(r'Data/changed_wav/changed_clam.wav','wav')#**代表转换后的wave文件名
data = wave.open(r"Data/changed_wav/changed_clam.wav")
