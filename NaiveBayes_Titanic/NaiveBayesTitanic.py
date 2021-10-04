# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:15:26 2021

@author: JYY
"""

import csv
import numpy as np


def dataProcess(filename='train.csv',a=0,b=1,c=4,d=5):
    '''读取csv文件'''
    train_data = []
    with open(filename,'r',newline='') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            train_data.append(line)
    '''将所需的特征重组成矩阵。每行为一个乘客，每列为乘客信息（编号，存活，性别，年龄）'''
    train = []
    male_age = female_age = 0
    male_num = female_num = 0
    for i in range(len(train_data)-1):
        train_row= []
        train_row.append(eval(train_data[i+1][a]))
        train_row.append(eval(train_data[i+1][b]))
        train_row.append(1 if train_data[i+1][c]=='male' else 0)
        age = train_data[i+1][d]
        if age.isdigit():
            train_row.append(eval(age))
            if train_row[2] == 1:
                male_num += 1
                male_age += eval(age)
            else:
                female_num += 1
                female_age += eval(age)
        else:
            train_row.append(-1)
        train.append(train_row)
    male_age = male_age/male_num
    female_age = female_age/female_num
    '''年龄————0（0~5）——1（6-15）——2（16-25）——3（26-35）——4（35-45）——5（45-...），默认3'''
    for i in range(len(train)):
        if train[i][3] == -1:
           train[i][3] = 3
        elif train[i][3] <=5:
            train[i][3] = 0
        elif train[i][3] <=15:
            train[i][3] =1
        elif train[i][3] <= 25:
            train[i][3] = 2
        elif train[i][3] <=35:
            train[i][3] =3
        elif train[i][3] <=45:
            train[i][3] = 4
        else:
            train[i][3] = 5
    return train


'''导入训练数据'''
train = dataProcess('train.csv',0,1,4,5)

'''计算先验概率和条件概率'''
sur = np.zeros(2)
sur_sex = np.zeros([2,2])
sur_age = np.zeros([2,6])
'''死——活''''''死——活————性别0~1''''''死——活————年龄0~6'''
for i in range(len(train)):
    sur[train[i][1]] += 1
    sur_sex[train[i][1]][train[i][2]] += 1
    sur_age[train[i][1]][train[i][3]] += 1
sur = sur/sur.sum()
for i in range(2):
    sur_sex[i] = sur_sex[i]/sur_sex[i].sum()
    sur_age[i] = sur_age[i]/sur_age[i].sum()
print(sur)
print(sur_sex)
print(sur_age)

'''导入测试数据'''
test = dataProcess('test.csv',0,0,3,4)

'''   '''
pre = []
for i in range(len(test)):
    precision_row = [str(test[i][0])]
    p_sur_0 = sur[0]*sur_sex[0][test[i][2]]*sur_age[0][test[i][3]]
    p_sur_1 = sur[1]*sur_sex[1][test[i][2]]*sur_age[1][test[i][3]]
    precision_row.append('0' if p_sur_0 > p_sur_1 else '1')
    pre.append(precision_row)
print(pre)
with open('precision.csv','w',newline='') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(['PassengerId','Survived'])
    csvwriter.writerows(pre)




        




        
    
# print(train)