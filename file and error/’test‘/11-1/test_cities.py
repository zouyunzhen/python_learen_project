#对city_functions.py进行测试。编写一个名为test_city_county()的方法(以’test_‘前缀开头的函数在继承unittest.TestCase的class)
#中会自动运行
#测试函数city_functions.py

import unittest
from city_functions import get_title_county

class GetTitleTest(unittest.TestCase):
    '''测试city_functions.py'''
    def test_print_title(self):
        '''一个方面，函数get_title_county是否会如我所愿？'''
        answer = get_title_county('county','city')
        self.assertEqual(answer,'City County')

