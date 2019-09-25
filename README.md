# interface_farmework
接口框架
添加一个公共方法  在入口文件调用这个方法  就会按照日期生成报告
import os
import time

class Pub():

    def mkdir(self):
        now = time.strftime('%Y-%m-%d')
        data_now = '../report/' + now
        isExits = os.path.exists(data_now)
        if not isExits:
            #os.makedirs(data_now)
            os.mkdir(data_now)
            the_path = os.path.abspath(data_now)
            return the_path
        else:
            the_path = os.path.abspath(data_now)
            return the_path

if __name__ == '__main__':
    tr = Pub().mkdir()
    print(tr)





from BSTestRunner import BSTestRunner  #测试报告模板
import time
import unittest2
from HTMLTestRunner import HTMLTestRunner

from comn.pubmth import Pub


test_dir = '../test_case'
#report_dir = '../report'
report_dir = Pub().mkdir()
discovery = unittest2.defaultTestLoader.discover(test_dir,pattern='test_*.py')
nowme = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = report_dir + '/' + nowme + 'result.html'

with open(report_name,'wb') as file:
    runner = BSTestRunner(stream=file,title='淘房中国 API 接口测试报告',description='interface descirption reports 接口报告具体展示信息')
    runner.run(discovery)
    file.close()
