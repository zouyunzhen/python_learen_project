#while loop 提示输入用户姓名。
#输入后打印一句问候语，且将一条到访记录添加到guest_book.txt文件中.确保这个文件中的每条记录都独自占一行

flag = True
while flag == True:
    guest_name = input('请输入姓名。\n')
    if guest_name == 'over':
        print('程序已关闭')
        break       #输入over时 ，会退出输入
    print('欢迎使用python',guest_name,'。')
    with open('guest.txt','a') as name:
        record = f'用户{guest_name}来访\n'
        name.write(record)