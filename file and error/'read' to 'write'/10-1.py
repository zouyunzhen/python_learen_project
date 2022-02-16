#读取文件learning_python,1,打印时读取整个文件2，打印时遍历整个文件3，打印时将各行存储在一个列表中，再用with代码块打印他们

filename = 'learning_python'
with open(filename) as filedata: #filedate 在此时表示的是一个表示文件learning_python的对象，运用print函数只会显示关于该文件的基本信息
    # 如字体格式等
    contents = filedata.read()#contents 这个盒子里现在才有了文件filedata 中的数据——一个很长的字符串
    print(contents.rstrip())#方法rstrip()清除这个很长的字符串最后位置的'\n',因为print函数自己会在最后加入一个'\n'，会重叠。
    print('over')

with open(filename) as filedata:
    for line in filedata:#初步估计是for循环的特性作为列表时逐个读取各个元素，是txt是逐个读取各行
        print(line.rstrip())#方法rstrip()清除这个很长的字符串最后位置的'\n',因为print函数自己会在最后加入一个'\n'，会重叠。
    print('over')

List = ''#创建一个空的字符串，是字符串
with open(filename) as filedata:
    for line in filedata.readlines():#filedata.readlines()现在表示的是个还没有赋值的列表，
                                    # readlines() 方法将filedata的数据作为一个按照行分元素的列表返回给了Python
        List += line#将各行内容加入字符串中
    print(List.rstrip())#方法rstrip()清除这个很长的字符串最后位置的'\n',因为print函数自己会在最后加入一个'\n'，会重叠。
    print('over')

