#简单DNS查询器—域名查询函数的设计

#1.用户需要选择是”1-查询域名”或是“2-查询IP地址”
#2.用户分别输入域名和IP地址
#3.如果输入的是IP地址，判断IP地址是否合法，调用check_ip()函数验证
#4.如果合法，调用dns_	query()函数，打开文件，查询域名或IP地址
#5.如果查询内容存在，返回查询完整条目
#6.如果查询内容不存在，返回没有找到。

#def dns_query (x,y)  #查询DNS记录
#def dns_query_main() #输入域名和IP地址，分割地址成列表，调用check_ip()和dns_query()
#if __name__==”__main__”:


#输入值来判断查询什么值
from check_ip import *

def dns_query():
    start = False
    while start == False:
        print('请选择查询类别：1-查询域名，2-查询IP地址')
        answer = input('请输入数字代码[1/2]')
        #如果输入1，则进行查询域名
        if answer == '1':
            #输入域名
            answer_address = input('请输入域名：')
            #打开文件
            file = open('hosts.txt', encoding='utf8')
            #再建立一个总列表
            file_all_list = file.readlines()
            #建立for循环，以空格分割域名和函数,并判断
            for i in file_all_list:
                address = i.split(' ')
                #遍历总列表，将子列表中[0]与输入值进行判断
                if address[0] == answer_address:
                    #此时如果存在[0]与输入值相等的，则返回域名加IP地址
                    print(f'查询成功，DNS记录为 {i}'.strip('\n'))
                    start = True
                    break
            else:
                #若不存在相等，则返回没有找到
                print('没有找到')

            #关闭文件
            file.close()
        elif answer == '2':
            #输入IP地址
            answer_ip = input('请输入IP地址：')
            #检查输入IP是否正确
            #输入不正确是没有办法逃出这个循环的
            falg = False
            while falg == False:
                falg = check_ip(answer_ip)
                if falg == False:
                    answer_ip = input('请输入IP地址：')
        #如果输入2，则进行查询IP地址
        #以空格分割域名和函数,并创建多个列表
            file0 = open('hosts.txt', encoding='utf8')
        #再建立一个总列表
            file_all_list0 = file0.readlines()
        #遍历总列表，将子列表中[1]与输入值进行判断
            for z in file_all_list0:
                address_ip = z.split(' ')
        #此时如果存在[1]与输入值相等的，则返回域名加IP地址
                if address_ip[1].strip('\n') == answer_ip.strip('\n'):
                    print(f'查询成功，DNS记录为 {z}'.strip('\n'))
                    start = True
                    break
            else:
                # 若不存在相等，则返回没有找到
                print('没有找到')

            file0.close()

        else:
            start = False
            print('输入数字错误，请重新输入！')
        #else，则输出“输入数字错误，请重新输入!”


if __name__ == "__main__":
    dns_query()
