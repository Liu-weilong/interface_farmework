#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/27 10:24
#@Author: liuweilong
#@File  : courier_interface.py
import unittest2
import requests
import time
from urllib import parse
import json

class Courier_Test(unittest2.TestCase):
    def setUp(self):
        self.base_url = 'http://www.kuaidi100.com/query?type=zhongtong'

    def test_courier(self):
        data = {'postid':'123456789'}
        res = requests.get(self.base_url,params=data)
        res_data = res.json()
        self.assertEqual(res_data['message'],'快递公司参数异常：单号不存在或者已经过期')

    def test_courier2(self):
        data = {'postid':'测试数据'}
        arr = parse.urlencode(data).encode('utf-8')
        res = requests.get(self.base_url,params=arr)
        res_data = res.json()
        self.assertEqual(res_data['message'],'参数错误')

    def test_courier3(self):
        data = {'postid':''}
        res = requests.get(self.base_url,params=data)
        res_data = res.json()
        self.assertEqual(res_data['status'],'400')

    def test_courier4(self):
        data = {'postid':'11111111111454564564564654654564654'}
        res = requests.get(self.base_url,params=data)
        res_data = res.json()
        self.assertEqual(res_data['message'],'快递公司参数异常：单号不存在或者已经过期')

    def test_courier5(self):
        data = {'postid':'75135258856231'}
        res = requests.get(self.base_url,params=data)
        res_data = res.json()
        self.assertEqual(res_data['message'],'ok')



if __name__ == '__main__':
    unittest2.main()