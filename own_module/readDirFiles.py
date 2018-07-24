# coding: cp932
import os

def readDirFiles(readDirPath):
    readDirFiles = os.listdir(readDirPath)
    movieNameArray = []
    for file in readDirFiles:
        if(file[-4:] == '.mp4'):
            movieNameArray.append(file[0:len(file)-4])
    return movieNameArray
