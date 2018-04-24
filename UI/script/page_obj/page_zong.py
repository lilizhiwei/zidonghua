from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import unittest

class page(object):
	'''用户登录页面'''

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
	def openpc(self):
		self.driver.get('http://www.yyddd.com/pc/login.html')
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def openmobile(self):
		self.driver.get('http://www.yyddd.com/mobile')

	#统一登录
	def user_login(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.pwd)
		self.driver.find_element_by_xpath("//*[@type='submit']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".remember"),"老板"))
		sleep(0.5)

	def user_login_xh(self):
		self.openpc()
		self.driver.find_element_by_id("loginAccount").send_keys(self.qx_user)
		self.driver.find_element_by_id("loginPassword").send_keys(self.qx_pwd)
		self.driver.find_element_by_xpath("//*[@type='submit']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".remember"),"李志伟小号"))
		sleep(0.5)

	def clickyg(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("员工").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[text()='业务员']"),"业务员"))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[text()='业务员']").click()
		sleep(0.5)

	def clickqx(self):
		a = self.driver.find_element_by_xpath("//*[text()='业务员']")
		ActionChains(self.driver).move_to_element(a).perform()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//div[@class='list-group-item listactive']//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//div[@class='list-group-item listactive']//i").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"//*[@aria-controls='goods']"),"商品业务"))
		sleep(0.5)

	def clickbc(self):
		self.driver.find_element_by_xpath("//button[@data-action='save']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content.layui-layer-padding"),"保存成功！"))
		sleep(0.5)

	#清空数据
	def clickqingkong(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cog']").click()
		self.driver.find_element_by_link_text("通用设置").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".padding-left-5")))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".padding-left-5").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//div/div/div[2]/div/button")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//div/div/div[2]/div/button").click()
		self.driver.find_element_by_xpath("//div[2]/div/button[2]").click()
		self.driver.find_element_by_css_selector(".layui-layer-input").send_keys(self.pwd)
		self.driver.find_element_by_css_selector(".layui-layer-btn0.pull-right").click()

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


