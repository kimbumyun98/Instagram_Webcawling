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
import pyautogui

# 01. 이미지 저장 폴더 설정
f_dir = input('이미지를 저장할 폴더(예:C:\\Users\\) : ')

# 02. 이미지 저장 계정 설정
guest = input('계정 : ')

# 03. 사용자 인스타 정보 설정
login_id = input('아이디 : ')
login_pw = input('비밀번호 : ')

# 04. 시간 설정
now = time.localtime()
f_name = '%04d-%02d-%02d-%02d-%02d-%02d' %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
dir_name = '사진저장'

# 05. 이미지 저장 폴더 설정
os.makedirs(f_dir+f_name+'-'+dir_name)
os.chdir(f_dir+f_name+'-'+dir_name)
f_result_dir=f_dir+f_name+'-'+dir_name

s_time = time.time()

# 06. 웹 열기
dr = webdriver.Chrome("C:/Users/KimBumYun/Desktop/Github/2023/Instagram_Webcawling/chromedriver.exe")
dr.set_window_size(1280, 1440)
dr.get('https://www.instagram.com/login')
time.sleep(2)

# 07. 로그인
id_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
pw_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

act = ActionChains(dr)
act.send_keys_to_element(id_box, login_id).send_keys_to_element(pw_box, login_pw).click(login_button).perform()
time.sleep(5)

# 08. 계정 들어가기
url = 'https://www.instagram.com/' + guest
dr.get(url)

# 09. 스크롤 내리기
SCROLL_PAUSE_TIME = 1
last_height = dr.execute_script("return document.body.scrollHeight")
timer = 1

'''
while (timer<10):
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    timer=timer+1
'''

while True:
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = dr.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

dr.execute_script('window.scrollTo(0, 0)')

count = 0
images = dr.find_elements(By.CSS_SELECTOR, 'img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3')
pyautogui.press('down', 7)

# 10. 이미지 다운로드
for image in images:
    try:
        imgUrl= dr.find_elements(By.CSS_SELECTOR, "img.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3")[count].get_attribute("src")
        print("다운로드 시작")
        urllib.request.urlretrieve(imgUrl, str(count)+".jpg")
        print("다운로드 완료")
        count = count+1

        if count % 3 == 0:
            pyautogui.press('down', 8)
    except:
        pass

e_time = time.time()#끝난시간 체크

t_time = e_time - s_time #크롤링에 쓰인 시간

print('='*80)
print('총 소요시간은 %s 초입니다.'%round(t_time, 1))
print('총 저장 건수는 %s 건입니다.'%count)
print('파일 저장 경로: %s 입니다.'%f_result_dir)
print('='*80)