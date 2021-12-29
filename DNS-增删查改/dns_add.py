#简单DNS查询器-域名添加函数的设计

from check_ip import *




def dns_add():
    # 输入域名，并赋值
    address = input('请输入域名：')
    # 输入IP地址，并赋值
    IP = input('请输入IP地址：')
    #应用ip_test函数
    flag = check_ip(IP)
    while flag == False:
        #输入IP地址，并赋值
        flag = check_ip(IP)
        if flag == False:
            IP = input('请输入IP地址：')

        
    
    #以添加模式，open文件hosts.txt
    file = open('hosts.txt','a',encoding='utf8')
    #重新赋值函数和域名为data
    data = f'{address} {IP}\n'
    #添加入host.txt中
    file.write(data)
    #写入完成
    file.close()
    #读文件
    file1 = open('hosts.txt',encoding='utf8')
    #以for循环遍历host.txt中的各个值并打印
    List = file1.readlines()
    print('hosts.txt文件内容为：')
    for i in List:
        print(i.strip('\n'))


    file1.close()
    input('dns记录添加完成，请输入任意键结束.....')

if __name__ == "__main__":
    dns_add()
    
    
    
