from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class daoru(page):

	#进入页面
	def clickkehu(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("客户").click()

	def clickghs(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-group']").click()
		self.driver.find_element_by_link_text("供货商").click()

	def clicksp(self):
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-cubes']").click()
		self.driver.find_element_by_link_text("商品库存").click()

	def clickX(self):
		self.driver.find_element_by_xpath("//*[@class='icon fa fa-file-excel-o']").click()
		sleep(0.5)

	def clickdaoru(self):
		self.driver.find_element_by_xpath("//*[@data-power='167']//i").click()

	def clickdaoru2(self):
		self.driver.find_element_by_xpath("//*[@data-power='176']//i").click()

	def clickdaoru3(self):
		self.driver.find_element_by_xpath("//*[@data-power='147']//i").click()

	def clickshang(self):
		WebDriverWait(self.driver,30,0.5).until(EC.visibility_of_element_located((By.XPATH,"//*[@class='fa fa-cloud-upload fa-4x fa-fw']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@class='fa fa-cloud-upload fa-4x fa-fw']").click()

	def clickshang2(self):
		self.driver.find_element_by_xpath("//*[@class='fa fa-refresh fa-4x fa-fw']").click()

	def clicktijiao(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".btn.btn-primary.margin-top-15.sender"),"确认提交"))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".fa.fa-check.fa-fw").click()

	def yanzheng(self):
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".layui-layer-content"),"导入完毕"))

	def clickwanbi(self):
		return self.driver.find_element_by_css_selector(".layui-layer-content").text

	def clickque(self):
		self.driver.find_element_by_link_text("确定").click()

	def dui(self):
		return self.driver.find_element_by_css_selector(".datasuccesslength").text

	def cuo(self):
		return self.driver.find_element_by_css_selector(".dataerrorlength").text
