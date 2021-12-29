#1.用户需要选择是”1-删除域名”或是“2-删除IP地址”
#2.用户分别输入域名和IP地址
#3.如果输入的是IP地址，判断IP地址是否合法，调用check_ip()函数验证
#4.如果合法，调用dns_	delete()函数，打开文件，删除域名或IP地址
#5.如果内容存在，删除后，打印删除成功，并显示被删除的完整条目
#6.如果删除内容不存在，返回没有找到。
#7.最后将删好的内容写入文件，并打印文件全部内容

#选择删除的对象1-域名，2-ip地址
#删除整个，包括域名和IP地址
#打印出删除后的有的值

from check_ip import *

def dns_delete():
    begin = False
    while begin == False:
        print('请选择删除类别：1-删除域名，2-删除IP地址')
        answer = input('请输入数字代码[1/2]')
        # if选择1-删除域名，or，2-删除IP地址
        if answer == '1':
            answer_name = input('请输入域名：')
            #打开文件，以读模式
            file = open('hosts.txt', encoding='utf8')
            #创建一个总列表
            file_all_list = file.readlines()
            file.close()
            #用以记录for循环到了哪一个元素
            number = -1
            #for循环进行与输入值的判断，True就调用del（）函数，结束循环
            for i in file_all_list:
                number += 1
                # 将子列表以空格分割成两个列表
                address = i.split(' ')
                #判断是否存在域名与输入值相等，若相等，就从file_all_list中删除
                if address[0] == answer_name:
                    #删除
                    del file_all_list[number]
                    #打开host.txt以写入模式
                    file_w = open('hosts.txt','w',encoding='utf8')
                    for z in file_all_list:
                        #写入剩下的内容
                        file_w.write(f'{z}')
                    file_w.close()
                    print(f'删除成功，DNS记录为 {i}'.strip('\n'))
                    print(f'现有记录如下：')
                    for a in file_all_list:
                        print(a.strip('\n'))
                    begin = True
                    break
            else:
                # 若不存在相等，则返回没有找到
                print('没有找到')
        elif answer == '2':
            answer_ip = input('请输入IP地址：')
            #调用check_ip函数
            #这是你绝对无法逃脱的验证
            start = False
            while start == False:
                start = check_ip(answer_ip)
                if start == False:
                    answer_ip = input('请输入IP地址：')
            # 打开文件，以读模式
            file0 = open('hosts.txt', encoding='utf8')
            # 创建一个总列表
            file_all_list0 = file0.readlines()
            file0.close()
            # 用以记录for循环到了哪一个元素
            number0 = -1
            # for循环进行与输入值的判断，True就调用del（）函数，结束循环
            for i in file_all_list0:
                number0 += 1
                # 将子列表以空格分割成两个列表
                ip = i.split(' ')
                # 判断是否存在域名与输入值相等，若相等，就从file_all_list中删除
                if ip[1].strip('\n') == {answer_ip}.strip('\n'):
                    # 删除
                    del file_all_list0[number0]
                    data = file_all_list0
                    # 打开host.txt以写入模式
                    file_w = open('hosts.txt', 'w', encoding='utf8')
                    for z in file_all_list0:
                        # 写入剩下的内容
                        file_w.write(f'{z}')
                    file_w.close()
                    print(f'删除成功，DNS记录为 {i}'.strip('\n'))
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
#else就显示没有找到

if __name__ == "__main__":
    dns_delete()