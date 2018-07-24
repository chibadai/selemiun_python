# coding: cp932
from time import sleep
from selenium import webdriver

def getYoutubeMovieUrl(chromeDriverPath, youtubeMovieUrl):

	sleepTime = 0.5

	driver = webdriver.Chrome(chromeDriverPath)
	driver.get(youtubeMovieUrl)

	sleep(sleepTime * 5)

	tmpTagNum = 0
	tagNum = 0
	tagNumCounter = 0
	for i in range(0, 1000):
		driver.execute_script("window.scrollBy(0, 1000);")
		tmpTag = driver.find_elements_by_tag_name("ytd-grid-video-renderer")
		tmpTagNum = len(tmpTag)
		if tmpTagNum > tagNum:
			tagNumCounter = 0
			tagNum = tmpTagNum
		elif tmpTagNum == tagNum:
			tagNumCounter += 1
		if tagNumCounter > 10:
			break
		sleep(sleepTime)

	youtubeWatchArray = []
	for youtubeWatchHTML in driver.find_elements_by_tag_name("ytd-grid-video-renderer"):
		try:
			youtubeWatchArray.append(youtubeWatchHTML.find_elements_by_css_selector('a')[0].get_attribute('href'))
		except:
			print('youtubeWatchHTML error')

	driver.close()
	return youtubeWatchArray
