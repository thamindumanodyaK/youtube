from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('C:\\Users\\ASUS TUF\\Downloads\\chromedriver_win32\\chromedriver')
linkList = []
firstLink = input("Enter the link of first video of the playlist : ")
count = int(input("how many videos do you want to download : "))
linkList.append(firstLink)
browser.get(firstLink)
for i in range(count):
    nextButton = browser.find_element(By.CLASS_NAME, "ytp-next-button.ytp-button")
    time.sleep(3)
    linkList.append(nextButton.get_attribute('href'))
    nextButton.click()

while len(linkList) != 0:
    browser.get('https://en.savefrom.net/')
    time.sleep(5)
    downloadLink = browser.find_element_by_id('sf_url')
    downloadLink.send_keys(linkList[0])
    downloadLink.send_keys(Keys.ENTER)
    time.sleep(15)
    try:
        downloadButton = browser.find_element(By.CLASS_NAME, "link.link-download.subname.ga_track_events.download-icon")
        downloadButton.click()
        time.sleep(5)
        del linkList[0]
    except:
        continue;

browser.close()





