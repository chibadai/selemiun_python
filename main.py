import sys, os
charDot = '.'
charUnderScore = '_'
charSpace = ' '
charSlash = '\\'
escakeTab = '\t'
charBlank = ''
charColon = ':'
currentDirPath = os.getcwd()
oneLevelBelowDirPath = currentDirPath + charSlash + 'own_module' + charSlash
sys.path.append(oneLevelBelowDirPath)

from own_module import OutputText
from own_module import Selenium
from own_module import readDirFiles
from own_module import transrater

youtubeMovieUrl = "https://www.youtube.com/user/mentalistdaigo/videos?sort=dd&view=0&shelf_id=8"
chromeDriverPath = oneLevelBelowDirPath + 'chromedriver.exe'
youtubeDlPath = oneLevelBelowDirPath + 'youtube-dl.exe'
ffmpegExePath = oneLevelBelowDirPath + 'ffmpeg.exe'
unexpectedErrorText = 'Unexpected error' + charColon
youtubeErrorText = 'youtube download error'
audioConvertErrorText = 'audio convert error'
speechToTextErrorText = 'speech to text error'
outputTextErrorText = 'output text error'
movieExtension = 'mp4'
audioExtension = 'wav'
txtExtension = 'txt'
movieNameStandard = charUnderScore + 'movie'
audioNameStandard = charUnderScore + 'audio'
zeroOne = '0'
zeroTwo = '00'
# select Output File Name
youtubeDlOptionCommand1 = '-o'
# select Output File Extension
youtubeDlOptionCommand2 = '-f' + charSpace + movieExtension
# overwrite Command
ffmpegOptionCommand1 = '-y'
# select Input File Command
ffmpegOptionCommand2 = '-i'
# Bit Rate Command
ffmpegOptionCommand3 = '-ab'
bitRate = '128k'

def main():
    OutputFileName = 'youtubeMovieCorrespondenceName.txt'
    # youtubeWatchArray = Selenium.getYoutubeMovieUrl(chromeDriverPath, youtubeMovieUrl)
    # ↓ test
    youtubeWatchArray = []
    youtubeWatchArray.append('https://www.youtube.com/watch?v=oVcpHosQ92g')
    youtubeWatchArray.append('https://www.youtube.com/watch?v=G2lObJWIwmY')
    # ↑ test
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
            counterName = charBlank + str(i)
        elif i > 9:
            counterName = zeroOne + str(i)
        else:
            counterName = zeroTwo + str(i)
        movieName = counterName + movieNameStandard + charDot + movieExtension
        audioName = counterName + audioNameStandard + charDot + audioExtension
        txtName = counterName + audioNameStandard + charDot + txtExtension
        youtubeMovieName.append(movieName)
        youtubeAudioName.append(audioName)
        audioOutputTxtName.append(txtName)
        correspondenceNameArray.append(youtubeWatchArray[i] + escakeTab + movieName + escakeTab + audioName + escakeTab + txtName)

    OutputText.outputText(OutputFileName, correspondenceNameArray)

    # youtube download
    for i in range(0, len(youtubeWatchArray)):
        try:
            youtubeDlCommandArray = []
            youtubeDlCommandArray.append(youtubeDlPath)
            youtubeDlCommandArray.append(youtubeWatchArray[i])
            youtubeDlCommandArray.append(youtubeDlOptionCommand1)
            youtubeDlCommandArray.append(youtubeMovieName[i])
            youtubeDlCommandArray.append(youtubeDlOptionCommand2)
            cmd = windowsCommandCreate(youtubeDlCommandArray)
            os.system(cmd)
        except:
            print(youtubeErrorText)
            print(unexpectedErrorText, sys.exc_info()[0])
            break

    # download movie convert wav
    for i in range(0, len(youtubeMovieName)):
        try:
            ffmpegConvertCommandArray = []
            ffmpegConvertCommandArray.append(ffmpegExePath)
            ffmpegConvertCommandArray.append(ffmpegOptionCommand1)
            ffmpegConvertCommandArray.append(ffmpegOptionCommand2)
            ffmpegConvertCommandArray.append(youtubeMovieName[i])
            ffmpegConvertCommandArray.append(ffmpegOptionCommand3)
            ffmpegConvertCommandArray.append(bitRate)
            ffmpegConvertCommandArray.append(currentDirPath + charSlash + youtubeAudioName[i])
            cmd = windowsCommandCreate(ffmpegConvertCommandArray)
            os.system(cmd)
        except:
            print(audioConvertErrorText)
            print(unexpectedErrorText, sys.exc_info()[0])
            break

    # convert audio create text
    for i in range(0, len(youtubeAudioName)):
        try:
            outputText = transrater.speechToText(currentDirPath + charSlash + youtubeAudioName[i])
            try:
                OutputFileName = audioOutputTxtName[i]
                OutputText.outputText(OutputFileName, outputText)
            except:
                print(outputTextErrorText)
                print(unexpectedErrorText, sys.exc_info()[0])
                break
        except:
            print(speechToTextErrorText)
            print(unexpectedErrorText, sys.exc_info()[0])
            break

    print('end')

def windowsCommandCreate(windowsCommandArray):
    command = ''
    for i in range(0, len(windowsCommandArray)):
        if i == 0:
            command = windowsCommandArray[i]
        else:
            command = command + charSpace + windowsCommandArray[i]
    return command

if __name__ == '__main__':
    main()
