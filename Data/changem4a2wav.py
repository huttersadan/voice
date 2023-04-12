from pydub import AudioSegment
import wave
import pylab as pl
import shutil
import os
m4a_path = 'C:\\Users\\hutter_sadan\\Documents\\录音'
for file_name in os.listdir(m4a_path):
    shutil.copyfile(m4a_path+'\\'+file_name,'D:\\part_job\\Real_Time_Speech_Emotion_Recognition\\Data\\changed_m4a\\'+file_name) 
ff_path = 'D:/downloads/ffmpeg-2023-04-06-git-b564ad8eac-essentials_build/bin/ffmpeg.exe'
AudioSegment.converter = ff_path
for single_m4a in os.listdir('D:\\part_job\\Real_Time_Speech_Emotion_Recognition\\Data\\changed_m4a'):
    song = AudioSegment.from_file('D:\\part_job\\Real_Time_Speech_Emotion_Recognition\\Data\\changed_m4a\\'+single_m4a)#路径可以使用绝对路径也可以使用相对路径
    song.export('Data/changed_wav/changed_{}.wav'.format(single_m4a[:-4]),'wav')#**代表转换后的wave文件名
    #data = wave.open(r"Data/changed_wav/changed_clam.wav")
