#使用方法count()确认特定的单词短语在字符串中出现了多少次。
    #注意。方法lower()可以将字符串中所有字母替换成小写，便于查找单词的所有的格式

with open('Final judgment.txt',encoding='utf-8') as book_1:
    book_1 = book_1.read()
    number = book_1.lower().count(' the ')
    print('据计算得到，已知的文章中一共有%s个“ the ”字。'%(number))

#使用open()函数时，当系统的默认编码与要读取文件使用的编码不一致时，必须给参数——encoding指定了值。初步判断时指定系统的默认编码即——'utf-8'
