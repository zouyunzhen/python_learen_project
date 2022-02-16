#加法运算
#用户输入的时文本时，使用int()函数会引发valueError（价值错误）。使用try-except-else关键字提醒用户输入错误
#用户输入后，将其相加并打印结果。

def judge_number(contents):
    try:
        contents = int(contents)
    except ValueError:
        print('What you type is not number!!!')#要注意顺序，在编程中，程序的执行顺序很关键
        return False
    else:
        return contents


contents_first = input('请输入首个数字\n')
contents_first = judge_number(contents_first)
contents_second = input('请输入第二个数字\n')
contents_second = judge_number(contents_second)


answer = contents_first + contents_second
print('您输入的数字之和是%s'%answer)
