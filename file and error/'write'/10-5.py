#while 循环，询问用户为何喜欢编程。每回答一个，就将其加入文件中。

flag = True
while flag == True:
    answer = input('你为什么喜欢编程？\n')
    if answer == 'over':
        print('程序已关闭')
        break       #输入over时 ，会退出输入
    with open('answer_programming','a') as why:
        why.write(answer+'\n')  #这里很重要，write方法中可用‘+’将变量和字符串连接到一起。但不能用‘,’