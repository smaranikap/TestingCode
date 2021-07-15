# import logging
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def setup(browser):
#     if browser=='chrome':
#         driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#         print("Launching chrome browser")
#     elif browser=='firefox':
#         driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
#         print("Launching firefox browser")
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


#
#
# class Test1:
#
#     @staticmethod
#     def runmethod():
#         logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s:%(levelname)s:%(message)s:',
#                             datefmt="%Y-%m-%d %H:%M:%S")
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
#
#
# # t = Test1()
# v = Test1.runmethod()
# v.info("8768668687")

# class test123:
#     url = "https://admin-demo.nopcommerce.com/"
#
#     def exe1(self,setup):
#         self.driver = setup
#         self.driver.get(self.url)
#         print("entered")

# from selenium import webdriver
# driver =  webdriver.Chrome(executable_path="C:\\chromedriver.exe")

# for i in range(3):
#     print(i)
#     driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#     driver.get("https://www.google.com/")
#     driver.close()

import random
import string

# n = random.randrange(1,1000)
# e = "Email_" + str(n) + "@gmail.com"

# print(e)

# def random_generator(size=8,chars=string.ascii_lowercase+string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
#
# v = random_generator()
# print(v)
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.maximize_window()
# var = WebDriverWait(dr,20).until(ec.visibility_of_element_located((By.XPATH,"//i[@class='nav-icon far fa-user']")))
#
# WebDriverWait(driver, 10).until(ec.invisibility_of_element_located((By.XPATH, "//input[@id='message']")))
# driver.find_element_by_link_text()
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
#
# driver =  webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.find_element_by_id("Email").clear()
# driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
# driver.find_element_by_id("Password").clear()
# driver.find_element_by_id("Password").send_keys("admin")
# driver.find_element_by_xpath("//button[@class='button-1 login-button']").click()
# WebDriverWait(driver,30).until(ec.visibility_of_element_located((By.XPATH,"//i[@class='nav-icon far fa-user']"))).click()
# WebDriverWait(driver,30).until(ec.visibility_of_element_located((By.XPATH,"//p[text()=' Customers']"))).click()
#
#
# tab = WebDriverWait(driver,30).until(ec.visibility_of_element_located((By.XPATH,"//table[@id='customers-grid']//tbody")))
# Rowc = len(driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr"))
#
# time.sleep(5)
# for i in range(1,Rowc+1):
#     Colc = len(driver.find_elements_by_xpath("//table[@id='customers-grid']//tbody/tr[" + str(i) +"]/td"))
#     for j in range(1,Colc):
#         xp = "//table[@id='customers-grid']//tbody/tr[" + str(i) +"]/td["+ str(j) +"]"
#         var = driver.find_element_by_xpath(xp).get_attribute('innerText')
#         if var =="brenda_lindgren@nopCommerce.com":
#             print("Exist")
#

# s = 'catandapple'
# print(s[:5])
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# x = slice(2,8,2)
# print(a[x])
# dict = {"name":["smaranika","rani"],"title":"parida"}
# print(dict.values())
# var1 = "smaranika"
# var2 = "rani7332"
# var3 = ""
# for i in var1:
#     if i not in var2:
#         var3 = var3+i
# print(var3)

# dict1 = {2:"smaranik",3:'parida'}
# print(dict1.get(2))
# dict1[4] = 'lekha'
#
# print(dict1)

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# import time
# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver.get("https://www.browserstack.com/guide/handling-tabs-in-selenium")
# driver.find_element_by_xpath("//a[@title='Selenium Testing'][1]").click()

# driver.execute_script("window.open('about:blank','secondtab');")
# driver.switch_to.window("secondtab")
# driver.get("https://www.facebook.com/")
# driver.execute_script("window.open('about:blank','thirdtab');")
# driver.switch_to.window("thirdtab")
# driver.get("https://mail.yahoo.com/d/folders/1/messages/96096?.intl=in&.lang=en-IN")
# for i in range(len(driver.window_handles)):
#     driver.switch_to.window(driver.window_handles[i])
#     if driver.find_elements_by_xpath("//a[text()='What is Automation Testing?']"):
#         print(driver.title)
#         driver.find_element_by_xpath("//a[text()='What is Automation Testing?']").click()

# driver.switch_to.window(driver.window_handles[-1])
# # print(len(driver.window_handles))
#
# WebDriverWait(driver,30).until(ec.visibility_of_element_located((By.XPATH,'//a[text()="What is Automation Testing?"]'))).click()
# driver.quit()
list1 = [2,3]
list2 = ['a','b']
dict1 = {2,3}

print(dct)

from selenium import webdriver
driver =  webdriver.Chrome(executable_path='c\\')
driver.get("google.com")
driver.execute_script("window.open('about:blank','secondtab');")
driver.get('path')
driver.switch_to.window('secondtab')
driver.switch_to.window(driver.window_handles[-1])