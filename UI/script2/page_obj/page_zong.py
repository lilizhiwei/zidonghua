from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import unittest

'''
self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*李志伟[\s\S]*") 
同IDE的verifyTextPresent  *李志伟*

self.assertNotRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*李志伟[\s\S]*") 
同IDE的verifyTextNotPresent  *李志伟*

WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"购物车空空如也"))
同IDE的waitForTextPresent  *购物车空空如也*
'''

class page(object):
	#用户登录页面

	username = '13140023070'
	password = '123456'
	qx_username = '13014625694'
	qx_password = '123456'

	def __init__(self, driver,user=username,pwd=password,qx_user=qx_username,qx_pwd=qx_password):
		self.user = user
		self.pwd = pwd
		self.qx_user = qx_user
		self.qx_pwd = qx_pwd
		self.driver = driver
		self.timeout = 30

	#打开网址
	def openbaidu(self):
		self.driver.get('http://www.baidu.com')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	#pc端保存成功
	def bccg(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"保存成功！"))
		sleep(0.5)
	
	#权限不足
	def qxbz(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"权限不足"))
		
	#移动端保存成功
	def bccg1(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@data-handler='ok']"),"确定"))
		self.driver.find_element_by_xpath("//*[@data-handler='ok']").click()


