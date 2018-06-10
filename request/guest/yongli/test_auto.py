import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class GetEventListTest(unittest.TestCase):

	''' 查询发布会信息（带用户认证）'''
	def setUp(self):
		self.base_url = "http://127.0.0.1:8000/api/sec_get_event_list/"
		self.auth_user = ('admin', 'admin123456')

	def test_get_event_list_auth_null(self):
		''' auth 为空 '''
		r = requests.get(self.base_url, params={'eid':''})
		result = r.json()
		self.assertEqual(result['status'], 10011)
		self.assertEqual(result['message'], 'user auth null')

	def test_get_event_list_auth_error(self):
		''' auth 错误 '''
		r = requests.get(self.base_url, auth=('abc','123'), params={'eid':''})
		result = r.json()
		self.assertEqual(result['status'], 10012)
		self.assertEqual(result['message'], 'user auth fail')

	def test_get_event_list_eid_null(self):
		''' eid 参数为空 '''
		r = requests.get(self.base_url, auth=self.auth_user, params={'eid':''})
		result = r.json()
		self.assertEqual(result['status'], 10021)
		self.assertEqual(result['message'], 'parameter error')

	def test_get_event_list_eid_success(self):
		''' 根据 eid 查询结果成功 '''
		r = requests.get(self.base_url, auth=self.auth_user, params={'eid':1})
		result = r.json()
		self.assertEqual(result['status'], 200)
		self.assertEqual(result['message'], 'success')
		self.assertEqual(result['data']['name'],u'红米Pro发布会')
		self.assertEqual(result['data']['address'],u'北京会展中心')

if __name__ == '__main__':
    test_data.init_data() # 初始化接口测试数据
    unittest.main()