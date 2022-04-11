from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver = Service("c://development/chromedriver.exe")

insta_mail = "9057086623"
insta_pass = "1gamer"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver)

    def login(self):
        self.driver.get("https://www.instagram.com/?hl=en")
        time.sleep(5)
        mail_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        mail_box.send_keys(insta_mail)
        time.sleep(5)
        pass_box = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        pass_box.send_keys(insta_pass)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        time.sleep(5)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(5)
        follower = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]'
                                                      '/a')
        follower.click()
        time.sleep(5)
        bar = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', bar)
        time.sleep(5)

    def follow(self):
        user_list = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]/ul')
        buttons = user_list.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            button.click()
            time.sleep(1)


hi = InstaFollower()
hi.login()
hi.find_followers()
hi.follow()
