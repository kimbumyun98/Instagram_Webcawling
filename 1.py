# 00. 라이브러리
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 01. 웹 열기
dr = webdriver.Chrome("C:/Users/KimBumYun/Desktop/Github/2023/Instagram_Webcawling/chromedriver.exe")
dr.set_window_size(414, 800)
dr.get('https://www.instagram.com/login')
time.sleep(2)

# 02. 로그인
id_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
pw_box = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
login_button = dr.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')

act = ActionChains(dr)
act.send_keys_to_element(id_box, 'kimbumyun').send_keys_to_element(pw_box, 'qjadbs980614').click(login_button).perform()
time.sleep(10)

pass_button = dr.find_element(By.XPATH, '//*[@id="mount_0_0_Lx"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
act.click(pass_button).perform()
time.sleep(60)