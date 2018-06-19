from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class baidu(page):

	#输入
	def shuru(self,name):
		self.driver.find_element_by_id("kw").send_keys(name)

	#点击
	def clickbd(self):
		self.driver.find_element_by_id("su").click()