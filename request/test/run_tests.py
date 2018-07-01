import time, sys
sys.path.append('./yongli')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data

'''
	def test_1(self):
        所有参数为空 
		payload = {'eid':'','name':'','limit':'','address':"",'start_time':''}
		r = requests.get(self.base_url, params=payload)
		r = requests.post(self.base_url, data=payload)
	    self.result = r.json()
	    self.assertEqual(self.result['status'], 200)
	    self.assertEqual(self.result['message'], 'success')
	    self.assertEqual(self.result['data'][0]['realname'],'alen')
	    self.assertEqual(self.result['data'][0]['phone'],'13511001100')

		{
		    "status": 200,
		    "message": "success",
		    "data": {
		        "eid": 220,
		        "name": "一加9手机发布会",
		        "limit": 2000,
		        "status": true,
		        "address": "深圳宝体",
		        "start_time": "2017-05-10T12:00:00"
		    }
		}
'''

if __name__ == "__main__":
	
    test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './html/' + now + '_result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')
    
    discover = unittest.defaultTestLoader.discover('./yongli',pattern='test_add_event.py')
    runner.run(discover)
    fp.close()