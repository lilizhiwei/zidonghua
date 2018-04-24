import time, sys
sys.path.append('./yongli')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
from db_fixture import test_data


if __name__ == "__main__":
	
    test_data.init_data() # 初始化接口测试数据

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './html/' + now + '_result.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况')

    # 指定测试用例为当前文件夹下的 yongli 目录
	discover = unittest.defaultTestLoader.discover('./yongli',pattern='*_test.py')
    runner.run(discover)
    fp.close()