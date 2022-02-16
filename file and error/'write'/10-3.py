#提示用户输入名字。用户做出响应后，将名字写入文件guest.txt中
guess_name = input('请输入姓名。\n')
with open('guest.txt', 'w') as name:
    name.write(guess_name)