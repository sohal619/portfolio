from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

promised_down = 50
promised_up = 50
twitter_mail = "sohalkhan90570@gmail.com"
twitter_password = "5d6L+I^l4Yw/q<7"
user = 'sohalkh93383327'

chrome_driver = Service("c://development/chromedriver.exe")


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                    '3]/div[1]/a')
        button.click()
        time.sleep(40)
        self.down = float((self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div['
                                                              '2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                              '2]/div/div[2]/span')).text)
        self.up = float((self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                            '3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
                                                            '3]/div/div[2]/span')).text)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(10)
        email_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                       '2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div['
                                                       '2]/div/input')
        email_box.send_keys(twitter_mail)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                         '2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]')
        next_button.click()
        time.sleep(15)
        pass_box = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                      '2]/div/div/div[2]/div[2]/div[1]/div/div/div['
                                                      '3]/div/label/div/div[2]/div[1]/input')
        pass_box.send_keys(twitter_password)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div['
                                                          '2]/div/div/div[2]/div[2]/div[2]/div/div[1]')
        login_button.click()
        time.sleep(10)
        tweet_box = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                       '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                       '1]/div/div/div/div/div/div/div/div/div/label/div['
                                                       '1]/div/div/div/div/div/div/div/div/div')
        tweet_box.send_keys(f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay "
                            f"for {promised_down}down/{promised_up}up?")
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '3]/div/div/div[2]/div[3]')
        tweet_button.click()


ist = InternetSpeedTwitterBot()
ist.get_internet_speed()
ist.tweet_at_provider()
