from time import sleep
from selenium import webdriver


sleepTime = 0.5

driver = webdriver.Chrome("D:/GitHub/selemiun_python/own_module/chromedriver.exe")
driver.get("https://www.youtube.com/user/mentalistdaigo/videos?sort=dd&view=0&shelf_id=8")

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
	youtubeWatchArray.append(youtubeWatchHTML.find_elements_by_css_selector('a')[0].get_attribute('href'))

driver.close()
