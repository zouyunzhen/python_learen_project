#编写的测试框架。包含方法test_give_default_raise()和test_give_coutom_raise()。
#运用了方法Setup().创立调查对象和答案列表。避免反复创建的风险

import unittest
from Employee_for_test import Employee

class TestEmployee_for_test(unittest.TestCase):
    '''测试类Employee'''

    def setUp(self):
        '''创建调查对象和答案列表'''
        first_name = 'zou'.title()
        second_name = 'jiacheng'.title()
        annual_salary = 9999999999
        #以上是调查对象的特征
        #下面是对象特征集合的实例
        self.empolyeeIn = Employee(second_name,first_name,annual_salary)
        #类Empolyee的各个函数输出的函数结果不一样不会重复。所以不在Setup中准备

    def test_forGetData(self):
        '''测试方法give_raise可否接受增加默认数额'''
        self.empolyeeIn.give_raise()
        self.assertEqual(10000004999,self.empolyeeIn.count_dollars)

    def test_forGetDataInMe(self):
        '''测试方法give_raise可否接受增加指定数额'''
        self.empolyeeIn.give_raise(1)
        self.assertEqual(10000000000,self.empolyeeIn.count_dollars)

if __name__ == '__main__':
    unittest.main()
