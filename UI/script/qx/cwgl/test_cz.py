from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
sys.path.append("../../page_obj")
from page_obj.qx_cwgl import cwgl
from page_obj.pc_daoru import daoru

class qxTest(unittest.TestCase):
	'''权限-充值测试'''

	def setUp(self):
		self.driver = webdriver.Chrome()

	def test_1shanchu(self):
		daoru(self.driver).user_login_xh()
		#新增充值单
		daoru(self.driver).clickkehu()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='221']//i")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='221']//i").click()
		self.driver.find_element_by_xpath("//*[@data-role='money']").send_keys(1)
		self.driver.find_element_by_xpath("//button[@data-action='save']").click()
		sleep(1)

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).cz_shanchu()
		cwgl(self.driver).clickbc()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-power="250"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="250"]').click()
		self.driver.find_element_by_xpath("//*[@class='number']/*[text()='1']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='删除']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='删除']").click()
		self.driver.find_element_by_link_text("确定").click()
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_2xiugai(self):
		daoru(self.driver).user_login_xh()

		#验证1
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-power="250"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="250"]').click()
		self.driver.find_element_by_xpath("//*[@class='number']/*[text()='1']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='删除']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-tips-title='删除']/..").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).cz_xiugai()
		cwgl(self.driver).cz_shanchu()
		cwgl(self.driver).clickbc()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-power="250"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="250"]').click()
		self.driver.find_element_by_xpath("//*[@class='number']/*[text()='1']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='编辑']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-tips-title='编辑']").click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@class="col-sm-9 col-sm-offset-3"]/button').send_keys(Keys.SPACE)
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_3xinzeng(self):
		daoru(self.driver).user_login_xh()

		#验证2
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-power="250"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="250"]').click()
		self.driver.find_element_by_xpath("//*[@class='number']/*[text()='1']").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-tips-title='编辑']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-tips-title='编辑']").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).cz_xiugai()
		cwgl(self.driver).cz_xinzeng()
		cwgl(self.driver).clickbc()

		#验证3
		daoru(self.driver).clickkehu()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='221']")))
		sleep(0.5)
		self.driver.find_element_by_xpath("//*[@data-power='221']").click()
		self.driver.find_element_by_xpath("//*[@data-role='money']").send_keys(1)
		self.driver.find_element_by_xpath("//button[@data-action='save']").click()
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')

	def test_4chakan(self):
		daoru(self.driver).user_login_xh()

		#验证3
		daoru(self.driver).clickkehu()
		self.driver.find_element_by_xpath("//td/*[@class='avatar avatar-online']/img").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@data-power='221']")))
		sleep(0.5)
		self.assertIn("hide",self.driver.find_element_by_xpath("//*[@data-power='221']").get_attribute("class"))

		#修改权限
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).cz_xinzeng()
		cwgl(self.driver).cz_chakan()
		cwgl(self.driver).clickbc()

		#验证4
		self.driver.find_element_by_xpath("//*[@class='site-menu-icon fa fa-rmb']").click()
		self.driver.find_element_by_link_text("资金帐户").click()
		WebDriverWait(self.driver,30,0.5).until(EC.presence_of_element_located((By.XPATH,'//*[@data-power="250"]')))
		sleep(0.5)
		self.driver.find_element_by_xpath('//*[@data-power="250"]').click()
		self.driver.find_element_by_xpath("//*[@class='number']/*[text()='1']").click()
		cwgl(self.driver).qxbz()
		self.assertEqual(self.driver.find_element_by_css_selector(".layui-layer-content.layui-layer-padding").text,'权限不足')
		
		#还原
		cwgl(self.driver).clickyg()
		cwgl(self.driver).clickqx()
		cwgl(self.driver).clickcwgl()
		cwgl(self.driver).clickquanxuan_czd()
		cwgl(self.driver).clickbc()

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()


