#使用方法replace()将字符串中的特定单词都替换成另一个单词

filename = 'learning_python'
with open(filename) as filedata:
    contents = filedata.read()
    contents = contents.replace('Python','C')
    #仅仅有contents.replace('Python','C')是不够的，此时的contents还是原来的contents
    #必须要改变，重新告诉电脑contents已经是被replace()方法改后的contents了
    print(contents.rstrip())
    print('over')

with open(filename) as filedata:
    for line in filedata:
        line = line.replace('Python','C')
        print(line.rstrip())
    print('over')

with open(filename) as filedata:
    contents = filedata.readlines()
    for line in contents:
        line = line.replace('Python','C')
        print(line.rstrip())
    print('over')
