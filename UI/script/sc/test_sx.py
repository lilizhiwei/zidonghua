from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os,random
sys.path.append("../page_obj")
from page_obj.page_sc import sc

class scSX(unittest.TestCase):
	'''商城-搜索筛选测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_sx(self):
		
		#pc端创建商品
		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name2 = str(a) + '商品1' + str(b)
		name3 = str(a) + '商品2' + str(b)
		name4 = str(a) + '套餐' + str(b)
		fl1 = str(a) + '大类' + str(b)
		fl2 = str(a) + '小类' + str(b)
		sc(self.driver).cj_sp1(name2)
		sc(self.driver).cj_sp3(name3,fl1,fl2)
		sc(self.driver).cj_tc(name4)
		sc(self.driver).sp_sj(name4)

		#商城验证
		sc(self.driver).opensc()
		sc(self.driver).ty_ss(name2)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".item-title"),name2))
		sleep(0.5)
		self.driver.refresh()
		sc(self.driver).sp_sx(fl2)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".item-title"),name3))
		sleep(0.5)
		sc(self.driver).sp_ck()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"有货"))
		sleep(0.5)
		sc(self.driver).sp_qx()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"规格参数"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥20~200[\s\S]*个/箱（1箱=10个）[\s\S]*品牌[\s\S]*iphone[\s\S]*") 
		sc(self.driver).opensc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".item-title"),name4))
		sleep(0.5)
		sc(self.driver).sp_ck()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"库存"))
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"套餐"))
		sleep(0.5)
		sc(self.driver).sp_qx()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,"/html"),"包含商品"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥40[\s\S]*%s[\s\S]*1个[\s\S]*" % name3) 
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*%s[\s\S]*" % name2) 

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()


