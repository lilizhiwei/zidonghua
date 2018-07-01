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
··		#代理
		proxies = {
		  "http": "http://10.10.1.10:3128",
		  "https": "http://10.10.1.10:1080",
		}
		r = requests.post(self.base_url, data=payload，proxies=proxies)
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

		r.status_code #响应状态码
		r.raw #返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read() 读取
		r.content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
		r.text #字符串方式的响应体，会自动根据响应头部的字符编码进行解码
		r.headers #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
		#*特殊方法*#
		r.json() #Requests中内置的JSON解码器
		r.raise_for_status() #失败请求(非200响应)抛出异常

		高级用法 ： http://docs.python-requests.org/en/latest/user/advanced/#advanced
		会话对象
		请求和响应对象
		准备好的请求
		SSL证书验证
		客户端证书
		CA证书
		正文内容工作流程
		活着
		流媒体上传
		块编码请求
		POST多个多部分编码文件
		事件挂钩
		自定义验证
		流式请求
		代理
		SOCKS
		合规
		编码
		HTTP动词
		自定义动词
		链接头
		运输适配器
		示例：特定的SSL版本
		阻止还是不阻止？
		标题排序
		超时
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