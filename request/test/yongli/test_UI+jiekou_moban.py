from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest,sys,os
import requests
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

# UI + 接口 结合脚本
class AddEventTest(unittest.TestCase):
    ''' 添加发布会 '''

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://127.0.0.1:8000/api/add_event/"

    def tearDown(self):
        self.driver.quit()

    def test_add_event_success11(self):
        self.driver.get('http://127.0.0.1:8000/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        sleep(2)
        self.driver.find_element_by_id("inputUsername").send_keys('admin')
        self.driver.find_element_by_id("inputPassword").send_keys('admin123456')
        sleep(1)
        self.driver.find_element_by_xpath("//*[@class='btn btn-lg btn-primary btn-block']").click()
        sleep(3)
        self.assertNotRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*一加4手机发布会[\s\S]*") 
        payload = {'eid':11,'name':'一加4手机发布会','limit':2000,'address':"深圳宝体",'start_time':'2017-05-10 12:00:00'}
        r = requests.post(self.base_url,data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'add event success')
        self.driver.refresh()
        sleep(5)
        self.assertRegexpMatches(self.driver.find_element_by_xpath("/html").text, r"[\s\S]*一加4手机发布会[\s\S]*")

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()
