import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep

path = Path(os.path.abspath(__file__))

class starting:
    def __init__(self,username,password):
        #ID AND PASSWORD
        self.username = username
        self.password = password
        self.path = path

        with open("userinfo.txt","w") as info:
            info.write(username)

        #APPLY OPTION TO WEBDRIVER
        self.driver = webdriver.Chrome(os.getcwd().replace("\\","/") + "/chromedriver.exe")
        self.driver.maximize_window()

    #OPEN IG LOGIN PAGE
    def open_Ig(self):
        self.driver.get("https://www.instagram.com/accounts/login")

    #TYPE USERNAME,PASSWORD TO TEXTBOXES AND CLICK TO LOGIN BUTTON
    def sign_In(self):    
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input'))).send_keys(self.username)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input'))).send_keys(self.password)
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div'))).click()

    #SET UP EVERYTHING AND GO TO HOMEPAGE OF IG OF THE USER
    def goToMainPage(self):
        WebDriverWait(self.driver,100).until(EC.visibility_of_element_located((By.XPATH,'/html/body/div[4]/div/div/div/div[3]/button[2]'))).click() 
        # sleep(3)
        # self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div').find_element_by_tag_name('button').click()

#✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓     START ALL DONE   ✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓✓