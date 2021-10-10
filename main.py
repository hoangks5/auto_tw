   
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import threading
import random

def khoitao():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    #chrome_options.headless = True
    return webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)
link = ''
def am():
    nb = int(input('Số nick cần chạy : '))
    link = input('Nhập link cần auto comment : ')
    thres = []
    for i in range(nb):
        thres.append(khoitao())
    for acc in thres:
        acc.get('https://twitter.com/i/flow/login')
        time.sleep(30)
    for acc in thres:
        acc.get(link)
    return thres
def coment(driver):
    time.sleep(5)
    try:
        while True:
            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[3]/div/div[1]/div').click()
            time.sleep(2)
            driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys('Alooo'+str(random.randint(0,100000)))
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[2]').click()
            time.sleep(5)
    except:
        driver.get(link)
        return coment(driver)
zzz = am()
def main(zzz):
    thes = []
    for acc in zzz:
        thes.append(threading.Thread(target=coment,args={acc,}))
    for zz in thes:
        zz.start()
    for zz in thes:
        zz.join()
main(zzz)
