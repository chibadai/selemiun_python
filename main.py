# coding: Shift_JIS
import sys, os
sys.path.append(os.getcwd() + "/own_module")
from own_module import OutputText
from own_module import Selenium
from own_module import readDirFiles

youtubeMovieUrl = "https://www.youtube.com/user/mentalistdaigo/videos?sort=dd&view=0&shelf_id=8"
chromeDriverPath = os.getcwd() + '/own_module/chromedriver.exe'
youtubeDlPath = os.getcwd() + '/own_module/youtube-dl.exe'

def main():
    # youtubeWatchArray = Selenium.getYoutubeMovieUrl(chromeDriverPath, youtubeMovieUrl)
    # OutputFileName = 'youtubeWatchUrl.txt'
    # OutputText.outputText(OutputFileName, youtubeWatchArray)
    # for i in range(0, len(youtubeWatchArray)):
    #     try:
    #         cmd = youtubeDlPath + ' ' + youtubeWatchArray[i]
    #         os.system(cmd)
    #         break
    #     except:
    #         print('youtube download error')

    movieNamesArray = readDirFiles.readDirFiles(os.getcwd())
    OutputFileName = 'youtubeMovieName.txt'
    OutputText.outputText(OutputFileName, movieNamesArray)
    for tmp in movieNamesArray:
        print(tmp)
    print('end')

if __name__ == '__main__':
    main()
