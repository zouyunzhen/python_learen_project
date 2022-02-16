#假设用户首次输入或者该用户不是上一次输入的用户
#为此需要在运行程序之前进行验证，确认该用户是源用户

import json
#独立的数字变量
n = 0

def judge():
    '''判断用户名是否与输入值相等'''
    filename = 'username.json'
    answer = input('用户名')
    try:
        with open(filename) as f:
            usesname = json.load(f)
    except FileNotFoundError:
        usesdata = '%6s' % 'user'
        with open(filename,'w') as f:
            json.dump(usesdata,f)
            usesdata = get()
            json.dump(usesdata,f)


def get():
    '''采集用户的数据'''
    answer_for_name = input('请输入您的用户名')
    user_data = '%6s' % answer_for_name
    return user_data

def find_for_data(user_data):
    '''提取用户数据'''
    data_in = user_data


