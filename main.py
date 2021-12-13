from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


class MyInfo:
    textbox_username_id = "txtUsername"
    textbox_password_id = "txtPassword"
    link = 'https://opensource-demo.orangehrmlive.com/'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.link)


    def setUserName(self, username):
        self.username_input = self.driver.find_element(By.ID, self.textbox_username_id)
        self.username_input.clear()
        self.username_input.send_keys(username)
        self.title = self.driver.title
        assert self.title == 'OrangeHRM'


    def setPassword(self, password):
        self.password_input = self.driver.find_element(By.ID, self.textbox_password_id)
        self.password_input.clear()
        self.password_input.send_keys(password)

    def button_click(self, button):
        self.driver.find_element(By.XPATH, button).click()

    def select(self, field, data):
        self.selectFielf = self.driver.find_element(By.XPATH, field)
        self.selectFielf.clear()
        self.selectFielf.send_keys(data)

    def filling(self, select, data):
        self.s = select.clear()
        self.s = select.send_keys(data)

    def delete_element(self, field):
        self.selectFielf2 = self.driver.find_element(By.XPATH, field).get_attribute('href')
        self.value = self.selectFielf2[(self.selectFielf2.index('=') + 1)::]
        self.srt = "ohrmList_chkSelectRecord_"
        self.srt += str(self.value)
        self.driver.find_element(By.ID, self.srt).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="btnDelete"]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="dialogDeleteBtn"]').click()

    def check_exists_by_xpath(self, xpath):
        try:
         self.driver.find_element(By.XPATH, xpath)
        except NoSuchElementException:
            return False
        return True
username = 'Admin'
password = 'admin123'
s = MyInfo()
s.setUserName(username)
s.setPassword(password)
s.button_click('//*[@id="btnLogin"]')  # press login
time.sleep(2)
s.button_click("/html/body/div[1]/div[2]/ul/li[1]/a/b")  # press admin
time.sleep(2)
s.button_click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/a")  # press job
time.sleep(2)
s.button_click("/html/body/div[1]/div[2]/ul/li[1]/ul/li[2]/ul/li[1]/a")  # press jobTitles
time.sleep(2)
s.button_click("/html/body/div[1]/div[3]/div[1]/div/div[2]/form/div[1]/input[1]")  # jobTitlesADD
time.sleep(2)
s.select('//*[@id="jobTitle_jobTitle"]', 'analyst')  # select and filling jobTitles
time.sleep(2)
s.select("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/textarea",
         'Analyze the behavior of store customers')  # select and filling jobDescription
time.sleep(2)
s.select("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/textarea",
         'I can work both remotely and in the office')  # jobNote
time.sleep(2)
s.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")  # press jobSave
time.sleep(2)
s.button_click("//*[contains(text(), 'analyst')]")  # press transition
time.sleep(2)
s.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")  # press edit_button
time.sleep(2)
s.select('//*[@id="jobTitle_jobTitle"]', 'designer')  # edit jobTitle
time.sleep(2)
s.select('//*[@id="jobTitle_jobDescription"]', 'create a site design')  # edit jobNote
time.sleep(2)
s.button_click("/html/body/div[1]/div[3]/div/div[2]/form/fieldset/p/input[1]")  # press edit_jobSave
time.sleep(2)
s.delete_element("//*[contains(text(), 'designer')]")  # delete element
time.sleep(2)
s.check_exists_by_xpath("//*[contains(text(), 'designer')]")  # examination
