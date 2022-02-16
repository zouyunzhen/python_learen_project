#继10-6后的改进

def judge_number(contents):
    '''整数化输入的文本，并给不是数字的文本以提示'''
    try:
        contents = int(contents)
    except ValueError:
        print('What you type is not number!!!')#要注意顺序，在编程中，程序的执行顺序很关键
        return False
    else:
        return contents


flag = True
while flag == True:
    contents_first = input('请输入首个数字\n')
    if contents_first == 'over':
        print('程序已退出')
        break
    contents_first = judge_number(contents_first)
    if contents_first == False:
        continue

    contents_second = input('请输入第二个数字\n')
    if contents_second == 'over':
        print('程序已退出')
        break
    contents_second = judge_number(contents_second)
    if contents_second == False:
        continue

    answer = contents_first + contents_second
    print('您输入的数字之和是%s' % answer)
    print("输入'over'退出")