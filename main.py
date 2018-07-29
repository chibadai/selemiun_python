# coding: Shift_JIS
import sys, os
sys.path.append(os.getcwd() + "/own_module")
from own_module import OutputText
from own_module import Selenium
from own_module import readDirFiles

youtubeMovieUrl = "https://www.youtube.com/user/mentalistdaigo/videos?sort=dd&view=0&shelf_id=8"
currentDirPath = os.getcwd()
oneLevelBelowDirPath = currentDirPath + '/own_module/
chromeDriverPath = oneLevelBelowDirPath + 'chromedriver.exe'
youtubeDlPath = oneLevelBelowDirPath + 'youtube-dl.exe'
ffmpegExePath = oneLevelBelowDirPath + 'ffmpeg.exe'
youtubeErrorText = 'youtube download error'
audioConvertErrorText = 'audio convert error'
movieExtension = 'mp4'
audioExtension = 'wav'
txtExtension = 'txt'
movieNameStandard = 'movie_'
audioNameStandard = 'audio_'
dot = '.'
charSpace = ' '
escakeTab = '\t'
OutputFileName = 'youtubeMovieCorrespondenceName.txt'
charBlank = ''
zeroOne = '0'
zeroTwo = '00'
# select Input File Command
ffmpegOptionComand1 = '-i'
# Bit Rate Command
ffmpegOptionComand2 = '-ab'
bitRate = '128'

def main():
    youtubeWatchArray = Selenium.getYoutubeMovieUrl(chromeDriverPath, youtubeMovieUrl)
    youtubeMovieName = []
    youtubeAudioName = []
    audioOutputTxtName = []
    correspondenceNameArray = []
    for i in range(0, len(youtubeWatchArray)):
        movieName = charBlank
        audioName = charBlank
        txtName = charBlank
        counterName = charBlank
        if i > 99:
            counterName = charBlank + i
        elif i > 9:
            counterName = zeroOne + i
        else:
            counterName = zeroTwo + i
        movieName = movieNameStandard + counterName + dot + movieExtension
        audioName = audioNameStandard + counterName + dot + audioExtension
        txtName = audioNameStandard + counterName + dot + txtExtension
        youtubeMovieName.append(movieName)
        youtubeAudioName.append(audioName)
        audioOutputTxtName.append(txtName)
        correspondenceNameArray.append(youtubeWatchArray[i] + escakeTab + movieName + escakeTab + audioName + escakeTab + txtName)

    OutputText.outputText(OutputFileName, correspondenceNameArray)

    # youtube download
    for i in range(0, len(youtubeWatchArray)):
        try:
            youtubeDlCommandArray = []
            commandArray.append(youtubeDlPath)
            commandArray.append(currentDirPath + youtubeWatchArray[i])
            commandArray.append(youtubeMovieName[i])
            cmd = windowsCommandCreate(commandArray)
            # cmd = youtubeDlPath + charSpace + currentDirPath + youtubeWatchArray[i] + charSpace + youtubeMovieName[i]
            os.system(cmd)
            break
        except:
            print(youtubeErrorText)

    # download movie convert wav
    for i in range(0, len(youtubeMovieName)):
        try:
            # cmd = ffmpegExePath + charSpace + ffmpegOptionComand + charSpace + youtubeMovieName[i] + charSpace + ffmpegOptionComand2 + charSpace + bitRate + charSpace + currentDirPath + youtubeAudioName
            ffmpegConvertCommandArray = []
            ffmpegConvertCommandArray.append(ffmpegExePath)
            ffmpegConvertCommandArray.append(ffmpegOptionComand)
            ffmpegConvertCommandArray.append(youtubeMovieName[i])
            ffmpegConvertCommandArray.append(ffmpegOptionComand2)
            ffmpegConvertCommandArray.append(bitRate)
            ffmpegConvertCommandArray.append(currentDirPath + youtubeAudioName)
            # cmd = windowsCommandCreate([ffmpegExePath, ffmpegOptionComand, youtubeMovieName[i], ffmpegOptionComand2, bitRate, (currentDirPath + youtubeAudioName)])
            cmd = windowsCommandCreate(ffmpegConvertCommandArray)
            os.system(cmd)
            break
        except:
            print(audioConvertErrorText)

    # convert audio create text

    # movieNamesArray = readDirFiles.readDirFiles(os.getcwd())
    # for tmp in movieNamesArray:
    #     print(tmp)

    print('end')
def windowsCommandCreate(windowsCommandArray):
    command = ''
    for i in range(0, len(windowsComandArray)):
        if i == 0:
            command = windowscommandArray[i]
        else:
            command = command + charSpace + windowscommandArray[i]

if __name__ == '__main__':
    main()
