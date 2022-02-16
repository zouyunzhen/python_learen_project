# 测试文件11-2中的函数

import unittest
from city_functions import get_title_county


class GetTitleTest(unittest.TestCase):
    '''测试city_functions.py'''

    def test_print_title(self):
        answer = get_title_county('county', 'city')
        self.assertEqual(answer, 'City，County - 5000')

if __name__ == '__main__':
    unittest.main()

