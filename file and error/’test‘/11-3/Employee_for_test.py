#创建一个名为Employee的类，方法__init__()接受名、姓和年薪，并将它们存储在属性中。
#创建方法give_raise(),默认增加年薪5000dollar,可以接受其他年薪增加量

class Employee:
    '''处理公司员工年薪增加的类'''
    def __init__(self,second_name,first_name,count_dollars):
        '''存储公司员工姓名，年薪'''
        self.second_name = second_name  #添加self.second即是重新创立这个类的属性。就像创立了一个新变量（关于此类的）一样
        self.first_name = first_name
        #如上面这个，self.first_name是一个叫first_name的这个类的属性
        self.count_dollars = count_dollars

    def give_raise(self,count_raise_money = 5000):
        '''增加年薪'''
        self.count_dollars += count_raise_money

    def show_me_count_money(self):
        '''打印年薪数量'''
        print(self.count_dollars)

