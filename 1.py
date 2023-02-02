# 00. 라이브러리
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
import urllib
import time
import random
import sys
import re
import os

# 01. 이미지 저장할 아이디 설정
f_dir = input('이미지를 저장할 폴더(예:C:\\Users) : ')
guest = input('계정 : ')
now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
dir_name = '사진저장'

os.makedirs(f_dir+f_name+'-'+dir_name)
os.chdir(f_dir+f_name+'-'+dir_name)
f_result_dir=f_dir+f_name+'-'+dir_name

print(f_result_dir)

s_time = time.time()
# 02. 웹 열기
dr = webdriver.Chrome("C:/Users/KimBumYun/Desktop/Github/2023/Instagram_Webcawling/chromedriver.exe")
dr.set_window_size(2560, 1440)
dr.get('https://www.instagram.com/login')
time.sleep(2)

# 03. 로그인
id_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
pw_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

act = ActionChains(dr)
act.send_keys_to_element(id_box, 'web_crawling_guest').send_keys_to_element(pw_box, '1q2w3e4r5t').click(login_button).perform()
time.sleep(5)

# 04. 계정 들어가기
url = 'https://www.instagram.com/' + guest
dr.get(url)

SCROLL_PAUSE_TIME = 1
last_height = dr.execute_script("return document.body.scrollHeight")
timer = 1
while (timer<10):
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    timer=timer+1
    time.sleep(1)

count = 0
images = dr.find_elements(By.CSS_SELECTOR, 'img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
time.sleep(4)

for image in images:
    try:
        time.sleep(4)
        imgUrl= dr.find_elements(By.CSS_SELECTOR, "img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")[count].get_attribute("src")
        print("다운로드 시작")
        urllib.request.urlretrieve(imgUrl,str(count)+".jpg")
        print("다운로드 완료")
        count = count+1
    except:
        pass

e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간

print('='*80)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%count)
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*80)