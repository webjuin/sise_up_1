# -*- coding: utf-8 -*-
import selenium
from selenium import webdriver
import pandas as pd
import os
import time
import sys
import matplotlib.pyplot as plt


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path='chromedriver_4664', options=options)

while True:
    os.system('cls')
    url_1 = 'https://finance.naver.com/'
    driver.get(url_1)
    codes = []
    names = []

    for i in range(1, 16):
        info_1 = driver.find_element_by_css_selector('#_topItems2 > tr:nth-child(' + str(i) + ') > th > a') # _topItems2
        code = info_1.get_attribute('href')[-6:]
        codes.append(code)
        name = info_1.get_attribute('innerText')
        names.append(name)

    #info_2 = driver.find_element_by_xpath('//*[@id="_topItems2"]/tr[1]/td[1]')
    #//*[@id="_topItems2"]/tr[1]/td[1]
    #price = info_2.get_attribute('innerText')

    #info_3 = driver.find_element_by_xpath('//*[@id="_topItems2"]/tr[1]/td[3]')
    #//*[@id="_topItems2"]/tr[1]/td[3]
    #up = info_3.get_attribute('innerText')

    df = pd.DataFrame({'code' : codes, 'name' : names})
    #df.to_excel('up.xlsx')
    print(df)
    #time.sleep(5000)
    
    #for code in codes:
    for cc in range(0, len(codes)):
        url_2 = 'https://finance.naver.com/item/sise.naver?code=' + str(codes[cc])
        driver.get(url_2)
        print(url_2)
        #driver.implicitly_wait(3)
        time.sleep(5)
        driver.switch_to.frame('day')
        trs = [3, 4, 5, 6, 7, 11, 12, 13, 14, 15]
        #trs = [3, 4]
        #/html/body/table[1]/tbody/tr[15]/td[1]/span
        #/html/body/table[1]/tbody/tr[15]/td[1]/span
        #/html/body/table[1]/tbody/tr[12]/td[1]/span
        #/html/body/table[1]/tbody/tr[7]/td[1]/span
        #/html/body/table[1]/tbody/tr[15]/td[2]/span
        #for td in range(1, 3):
        #    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[' + str(td) + ']/a')
        price = []
        for tr in trs:
            tt = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[' + str(tr) + ']/td[1]/span')
            c1 = tt.get_attribute('innerText')
            open = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[' +str(tr) + ']/td[2]/span')
            c2 = open.get_attribute('innerText')
            aa = int(c2.replace(',',''))
            price.append(aa)
            print(codes[cc], names[cc], c1, c2)

        #print(type(price)
        #plt.plot(price)
        #plt.pause(1)
        #plt.clf()
        
