import sys, os
ffmpegDlPath = os.getcwd() + '\own_module\\ffmpeg.exe'

try:
    convertFileName = 'test.mp4'
    cmd = ffmpegDlPath + ' -i ' + convertFileName + '-ab 128 ' + os.getcwd() + 'test.wav'
    os.system(cmd)
except:
    print('audio convert error')
