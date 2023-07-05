import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "pencil_drawing_art_0"
USERNAME = "**********"
PASSWORD = "**********"

class InstaFollower:
    def __init__(self, path):
        self.service = Service(executable_path=path)
        self.driver = webdriver.Chrome(service= self.service)

    def login(self):
        URL = "https://www.instagram.com/accounts/login/"
        self.driver.get(url=URL)
        self.driver.maximize_window()

        time.sleep(2)

        username = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)

        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        print("Second Function called")
        URL = "https://www.instagram.com/pencil_drawing_art_0/"
        self.driver.get(url=URL)

        time.sleep(5)

        followers_btn = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_XE"]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
        followers_btn.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        followers = self.driver.find_elements(By.CSS_SELECTOR, "li button" )
        for follower in followers:
            try:
                follower.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel.click()


User = InstaFollower(CHROME_DRIVER)
User.login()
User.find_followers()
User.follow()