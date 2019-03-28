#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/27 10:54
#@Author: liuweilong
#@File  : run.py
import time
from BSTestRunner import BSTestRunner
import unittest2

test_dir = './test_case'
report_dir = './test_report'
discovery = unittest2.defaultTestLoader.discover(test_dir,pattern='courier_interface.py')
now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = report_dir + '/' + now +  'result.html'
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='API Test Report',description='Interface Test Results')
    runner.run(discovery)
    f.close()
# if __name__ == '__main__':
#     unittest2.main()
