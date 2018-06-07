from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
from .page_zong import page
import unittest

class cwgl(page):

	#进入页面
	def clickcwgl(self):
		self.driver.find_element_by_xpath("//*[@aria-controls='finance']").click()

	def clickquanxuan_zh(self):
		self.driver.find_element_by_xpath("//div/span[text()='结算账户']/../button").click()

	def clickquanxuan_zcd(self):
		self.driver.find_element_by_xpath("//div/span[text()='支出单']/../button").click()
	
	def clickquanxuan_srd(self):
		self.driver.find_element_by_xpath("//div/span[text()='收入单']/../button").click()

	def clickquanxuan_zzd(self):
		self.driver.find_element_by_xpath("//div/span[text()='账户转账']/../button").click()

	def clickquanxuan_czd(self):
		self.driver.find_element_by_xpath("//div/span[text()='收款/充值单']/../button").click()

	def clickquanxuan_fkd(self):
		self.driver.find_element_by_xpath("//div/span[text()='付款单']/../button").click()
		
	def zh_chakan(self):
		self.driver.find_element_by_id("260").click()

	def zh_xinzeng(self):
		self.driver.find_element_by_id("261").click()

	def zh_xiugai(self):
		self.driver.find_element_by_id("262").click()

	def zh_shanchu(self):
		self.driver.find_element_by_id("263").click()

	def zc_chakan(self):
		self.driver.find_element_by_id("200").click()

	def zc_xinzeng(self):
		self.driver.find_element_by_id("201").click()

	def zc_xiugai(self):
		self.driver.find_element_by_id("202").click()

	def zc_shanchu(self):
		self.driver.find_element_by_id("203").click()

	def sr_chakan(self):
		self.driver.find_element_by_id("210").click()

	def sr_xinzeng(self):
		self.driver.find_element_by_id("211").click()

	def sr_xiugai(self):
		self.driver.find_element_by_id("212").click()

	def sr_shanchu(self):
		self.driver.find_element_by_id("213").click()

	def zz_chakan(self):
		self.driver.find_element_by_id("240").click()

	def zz_xinzeng(self):
		self.driver.find_element_by_id("241").click()

	def zz_xiugai(self):
		self.driver.find_element_by_id("242").click()

	def zz_shanchu(self):
		self.driver.find_element_by_id("243").click()

	def zj_chakan(self):
		self.driver.find_element_by_id("250").click()

	def zj_chakan_quanxuan(self):
		self.driver.find_element_by_xpath("//div/span[text()='资金流水']/../button").click()

	def cz_chakan(self):
		self.driver.find_element_by_id("220").click()

	def cz_xinzeng(self):
		self.driver.find_element_by_id("221").click()

	def cz_xiugai(self):
		self.driver.find_element_by_id("222").click()

	def cz_shanchu(self):
		self.driver.find_element_by_id("223").click()

	def fk_chakan(self):
		self.driver.find_element_by_id("230").click()

	def fk_xinzeng(self):
		self.driver.find_element_by_id("231").click()

	def fk_xiugai(self):
		self.driver.find_element_by_id("232").click()

	def fk_shanchu(self):
		self.driver.find_element_by_id("233").click()

	