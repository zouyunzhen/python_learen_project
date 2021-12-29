#四个列表，找出在列表中最大的一个
#又要找出在列中最大的一个

#生成四个包含四个随机数的列表
import random

List1 = []
List2 = []
List3 = []
List4 = []
List = [List1,List2,List3,List4]
List_for_judge = []



for i in List:
    for z in range(1,5):
        #循环四次
        i.append(random.randint(10,100))

#显示
print(List1)
print(List2)
print(List3)
print(List4)
flag = False

#找出一个列表中的最大值和它的索引
for a in List:
    List_max =  max(a)
    number = 0
    for l in a:
        #开始判断索引
        List_max_index = l
        if List_max == List_max_index:
            for a in List:
                List_for_judge.append(a[number])
                long = len(List_for_judge)
                if long == 4:
                    List_judge_min = min(List_for_judge)
                    List_for_judge = []
                    if List_judge_min == List_max:
                        print('我找到了%s'%List_max)
                        flag = True
        else:
            #number用于确认索引
            number += 1
    #接下来，将所有列的数据加入进去
if flag == False:
    print('我没有发现')