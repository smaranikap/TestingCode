# from Test1.Testing import Test2
#
# v= Test2.runmethod()
# v.info("Testing")
# v.warning("testing warning new")
# from selenium import webdriver
# import pytest
#
# @pytest.fixture()
# def setup(browser):
#     if browser=='Chrome':
#         driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#         print("Launching chrome browser")
#     elif browser=='firefox':
#         driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")
#         print("Launching firefox browser")
#     else:
#         driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#     return driver
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")


