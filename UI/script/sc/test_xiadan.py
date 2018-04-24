from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,random,os
sys.path.append("../page_obj")
from page_obj.pc_daoru import daoru
from page_obj.page_sc import sc

class scXD(unittest.TestCase):
	'''商城-下单测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

		sc(self.driver).user_login()
		a = random.randint(0,1000)
		b = random.randint(0,1000)
		name1 = str(a) + '李志伟' + str(b)
		bh1 = str(a) + str(b)
	def test_1xd(self):

		#新建密码编号客户及两商品一套餐
		name2 = str(a) + '商品1' + str(b)
		name3 = str(a) + '商品2' + str(b)
		name4 = str(a) + '套餐' + str(b)
		sc(self.driver).cj_kh(name1,bh1)
		sc(self.driver).cj_sp1(name2)
		sc(self.driver).cj_sp2(name3)
		sc(self.driver).cj_tc(name4)
		sc(self.driver).sp_sj(name4)
		
		#进入商城下单
		#三个全加入购物车，然后删除一个，最后结算
		sc(self.driver).loginsc(bh1)
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).tj_sp2()
		sc(self.driver).clickdw()
		sc(self.driver).jr_gwc()
		sc(self.driver).tj_sp3()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"3"))
		sleep(0.5)
		sc(self.driver).clicksc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsPrice'),"240"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz2()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"购物车空空如也"))
		sleep(0.5)
		sc(self.driver).sc_dd()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"￥240"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥240[\s\S]*")


		#pc端验证订单并转为销售单
		sc(self.driver).user_login()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("订单历史").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.title'),name1))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".title").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"销售订单 [未完成]"))
		sleep(1)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*%s[\s\S]*来　源：商城[\s\S]*河南商丘[\s\S]*13523148316[\s\S]*尾　款：240[\s\S]*备注：尽快送货[\s\S]*总计： 240[\s\S]*" % name1)
		self.driver.find_element_by_link_text("转为销售单").click()
		self.driver.find_element_by_link_text("确定").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"实收：240"))
		sleep(0.5)
		self.driver.find_element_by_xpath('//nav/div[2]//*[@class="bg-blue-600 white submit"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"保存成功"))


		#再次商城验证订单
		sc(self.driver).loginsc(bh1)
		sc(self.driver).sc_dd()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"暂无数据"))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@href="#already"]').click()
		sleep(0.5)
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"￥240"))
		sleep(0.5)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*￥240[\s\S]*")


	def test_2xd_nm(self):
		#匿名下单并验证
		sc(self.driver).openpc()
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).tj_sp2()
		sc(self.driver).clickdw()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"2"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.uName')))
		sleep(0.5)
		self.driver.find_element_by_css_selector('.uName').click()
		sc(self.driver).shdz3()
		sc(self.driver).liuyan()
		self.driver.find_element_by_css_selector('.col-30>div').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"购物车空空如也"))

		#pc端验证
		sc(self.driver).user_login()
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-sign-out']").click()
		self.driver.find_element_by_link_text("订单历史").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.title'),"零散客户"))
		sleep(0.5)
		self.driver.find_element_by_css_selector(".title").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"销售订单 [未完成]"))
		sleep(1)
		self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*来　源：商城[\s\S]*河南商丘[\s\S]*13523148316[\s\S]*尾　款：240[\s\S]*备注：尽快送货[\s\S]*总计： 240[\s\S]*")
		self.driver.find_element_by_link_text("转为销售单").click()
		self.driver.find_element_by_link_text("确定").click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"实收：240"))
		sleep(0.5)
		self.driver.find_element_by_xpath('//nav/div[2]//*[@class="bg-blue-600 white submit"]').click()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.XPATH,'/html'),"保存成功"))


		#再次商城验证
		sc(self.driver).opensc()
		sc(self.driver).tj_sp1()
		sc(self.driver).jr_gwc()
		sc(self.driver).clickgwc()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.goodsNumber'),"1"))
		sleep(0.5)
		sc(self.driver).clicktj()
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.uName'),"李志伟"))
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.uTel'),"13523148316"))
		WebDriverWait(self.driver,30,0.5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.item-subtitle.uAddress'),"河南商丘"))

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()


