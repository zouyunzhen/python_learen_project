#1.用户需要选择是”1-修改域名”或是“2-修改IP地址”
#2.用户分别输入原域名/新域名和原IP地址/新IP地址
#3.如果输入的是IP地址，判断IP地址是否合法，调用check_ip()函数验证
#4.如果合法，调用dns_modify()函数，打开文件，修改域名或IP地址
#5.如果内容存在，修改后打印修改成功，并显示被修改的最终条目
#6.如果修改内容不存在，返回没有找到。
#7.最后将改好的内容写入文件，并打印文件全部内容

from check_ip import *

def dns_modify():
    begin = False
    while begin == False:
        print('请选择修改类别：1-修改域名，2-修改IP地址')
        answer = input('请输入数字代码[1/2]')
        # if选择1-删除域名，or，2-删除IP地址
        if answer == '1':
            answer_name = input('请输入原域名：')
            # 打开文件，以读模式
            file = open('hosts.txt', encoding='utf8')
            # 创建一个总列表
            file_all_list = file.readlines()
            file.close()
            # 用以记录for循环到了哪一个元素
            number = -1
            # for循环进行与输入值的判断
            for i in file_all_list:
                number += 1
                # 将子列表以空格分割成两个列表
                address = i.split(' ')
                # 寻找域名与输入值相等
                if address[0] == answer_name:
                    new_name = input('请输入新域名：')
                    address[0] = new_name
                    #告诉他，他现在已经不再是列表了，string
                    data = f'{address[0]} {address[1]}'
                    file_all_list[number] = data
                    # 打开host.txt以写入模式
                    file_w = open('hosts.txt', 'w', encoding='utf8')
                    for z in file_all_list:
                        # 写入剩下的内容
                        file_w.write(f'{z}')
                    file_w.close()
                    print(f'修改成功，原DNS记录改为 {data}'.strip('\n'))
                    print(f'现有记录如下：')
                    for a in file_all_list:
                        print(a.strip('\n'))
                    begin = True
                    break

            else:
                # 若不存在相等，则返回没有找到
                print('没有找到')

        elif answer == '2':
            answer_ip = input('请输入原IP地址：')
            # 这是你绝不可能掏出的循环
            flag = False
            while flag == False:
                flag = check_ip(answer_ip)
                if flag == False:
                    answer_ip = input('请输入原IP地址：')
            # 打开文件，以读模式
            file0 = open('hosts.txt', encoding='utf8')
            # 创建一个总列表
            file_all_list0 = file0.readlines()
            file0.close()
            # 用以记录for循环到了哪一个元素
            number0 = -1
            # for循环进行与输入值的判断
            for i in file_all_list0:
                number0 += 1
                # 将子列表以空格分割成两个列表
                ip = i.split(' ')
                # 寻找域名与输入值相等
                if ip[1].strip('\n') == answer_ip.strip('\n'):
                    new_name = input('请输入新IP地址：')
                    #这是你绝不可能逃出的循环
                    flag0 = False
                    while flag0 == False:
                        flag0 = check_ip(new_name)
                        if flag0 == False:
                            new_name = input('请输入新IP地址：')
                    #ip[1]此时为new_name\n!
                    trouble = '\n' in ip[1]
                    if trouble == True:
                        ip[1] = f'{new_name}\n'
                    else:
                        ip[1] = f'{new_name}'
                    # 告诉他，他现在已经不再是列表了，string
                    data = f'{ip[0]} {ip[1]}'
                    file_all_list0[number0] = data
                    # 打开host.txt以写入模式
                    file_w = open('hosts.txt', 'w', encoding='utf8')
                    for z in file_all_list0:
                        # 写入剩下的内容
                        file_w.write(z)
                    file_w.close()
                    print(f'修改成功，原DNS记录改为 {data}'.strip('\n'))
                    print(f'现有记录如下：')
                    for a in file_all_list0:
                        print(a.strip('\n'))
                    begin = True
                    break

            else:
                # 若不存在相等，则返回没有找到
                print('没有找到')

        else:
            begin = False
            print('输入数字错误，请重新输入！')

if __name__ == "__main__":
    dns_modify()