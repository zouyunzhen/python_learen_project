#提示用户输入喜欢的数字并存储
#然后再读取打印

import json
def get():
    '''提示用户输入喜欢的数字，并存储'''
    answer = input("What's your favorite number?\n")
    filename = 'favorite numbers.json'
    with open(filename,'w') as f:
        json.dump(answer,f)#先打入要存入的数据，然后再打入被存储文件的在python中的变量名
        print("I'will remember you")

def get_data():
    '''如果存在，获取用户输入的值'''
    filename = 'favorite numbers.json'
    try:
        with open(filename) as f:
            favorite_numbers = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_numbers

def out():
    '''打印用户输入的值'''
    number = get_data()
    if number:
        print(f'your favorite number is {number}')
    else:
        get()

out()