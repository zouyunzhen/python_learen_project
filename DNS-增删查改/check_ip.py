# 判断IP地址合法性
#check_ip.py
def check_ip(IP):
    start = True
    flag = True
    while start == True:

        # 拆分IP地址，形成部分来判断
        IP_part = IP.split('.')

        # 判断地址有无数字外字母
        for i in IP_part:
            answer = i.isdigit()
            if answer == False:
                print('你输入的IP地址有非数字')
                flag = False
                break

        #结束判断
        if flag == False:
            return False
            break

        # 判断地址长度
        IP_lenghthen = len(IP_part)
        if IP_lenghthen != 4:
            print('您输入的IP地址长度有误!!!!!,应该为“xxx.xxx.xxx.xxx”')
            flag = False

        #结束判断
        if flag ==False:
            return False
            break


        # 判断地址有无超出范围
        for z in IP_part:
            if int(z) > 255 or int(z) < 0:
                print('你输入的地址超出正常范围!!!!!,应该在"0.0.0.0--255.255.255.255之间"')
                flag = False
                break

        #结束判断
        if flag == False:
            return False
            break

        if flag == True:
            
            return True


# 循环输入IP地址
def check_ip_main():
    flag = True
    while flag == True:
        IP = input('请输入IP地址：')
        answer3 = check_ip(IP)
        if answer3 == True:
            break


if __name__ == "__main__":
    check_ip_main()
