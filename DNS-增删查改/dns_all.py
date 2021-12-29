from dns_modify import *
from dns_delete import *
from dns_query import *
from dns_add import *
from check_ip import *

start = False

while start == False:
    print('请选择DNS记录操作类别：1-查询，2-添加，3-修改，4-删除')
    answer = int(input('请输入数字代码[1/2/3/4]'))
    #开始调用
    if answer == 1:
        dns_query()
        start = True
        print('DNS操作结束！')
    elif answer == 2:
        dns_add()
        start = True
        print('DNS操作结束！')
    elif answer == 3:
        dns_modify()
        start = True
        print('DNS操作结束！')
    elif answer == 4:
        dns_delete()
        start = True
        print('DNS操作结束！')
    else:
        start = False
        print('输入数字错误，请重新输入！')

