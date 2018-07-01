from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.page_baidu import baidu
from page_obj.page_zong import page

class qxTest(unittest.TestCase):
	'''百度搜索'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1sousuo(self):
		baidu(self.driver).openbaidu()
		baidu(self.driver).shuru('python')
		baidu(self.driver).clickbd()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"百度为您"))
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@class="nums_text"]')))
		sleep(0.5)
		self.assertEqual(self.driver.find_element_by_css_selector(".nums_text").text,'百度为您找到相关结果约100,000,000个')
		self.assertEqual(self.driver.find_element_by_xpath('//*[@class="nums_text"]').text,'百度为您找到相关结果约100,000,000个')
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*百度为您找到相关结果[\s\S]*") 

	def test_2sousuo(self):
		baidu(self.driver).openbaidu()
		
	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()