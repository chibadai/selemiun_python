import sys, os
ffmpegDlPath = os.getcwd() + '\own_module\\ffmpeg.exe'

try:
    convertFileName = '★性体験が増える性格とは〜最新科学が明かすえげつないモテ技術-unx2o_4B2n8.mp4'
    cmd = ffmpegDlPath + ' -i ' + convertFileName + '-ab 128 ' + os.getcwd() + 'test.wav'
    os.system(cmd)
except:
    print('audio convert error')
