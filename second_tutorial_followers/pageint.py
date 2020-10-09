from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox(executable_path='C:/Users/wesleygurgel/Downloads/geckodriver.exe')
        time.sleep(5)

    # Function will log us in to Instagram
    def login(self):
        bot = self.bot
        # Navigate to the Instagram login page
        bot.get('https://www.instagram.com/accounts/login/')
        time.sleep(3)

        # Find the email and password boxes, enter our login credentials
        email = bot.find_element_by_name('username').send_keys(self.username)
        password = bot.find_element_by_name('password').send_keys(self.password)

        # Wait for 1 second then press ENTER
        time.sleep(1)
        bot.find_element_by_name('password').send_keys(Keys.RETURN)

        # Wait 3 second while the post-login page loads
        time.sleep(3)


    def follower_bikeaventura(self):
        bot = self.bot
        bot.get('https://www.instagram.com/neymarjr/')
        time.sleep(2)

        bot.find_element_by_xpath('//a[@href="/neymarjr/followers/"]').click()
        time.sleep(3)

        while bot.find_element_by_xpath("//button[contains(text(), 'Seguir')]"):
            pessoa = bot.find_element_by_xpath("//button[contains(text(), 'Seguir')]")
            bot.execute_script("arguments[0].click();", pessoa)
            time.sleep(10)

            pessoas_comseguir = bot.find_elements_by_xpath("//button[contains(text(), 'Seguir')]")
            if len(pessoas_comseguir) <= 1:
                popup = bot.find_element_by_class_name('isgrP')
                bot.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', popup)
                time.sleep(1)



insta = InstagramBot('testewithpython', '71txkq')
insta.login()
insta.follower_bikeaventura()