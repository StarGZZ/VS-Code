import random
import openpyxl,time
import datetime

def p_random(arr1,arr2):
    assert len(arr1) == len(arr2), "Length does not match."
    assert sum(arr2) == 1 , "Total rate is not 1."

    sup_list = [len(str(i).split(".")[-1]) for i in arr2]
    top = 10 ** max(sup_list)
    new_rate = [int(i*top) for i in arr2]
    rate_arr = []
    for i in range(1,len(new_rate)+1):
        rate_arr.append(sum(new_rate[:i]))
    rand = random.randint(1,top)
    data = None
    for i in range(len(rate_arr)):
        if rand <= rate_arr[i]:
            data = arr1[i]
            break
    return data

money = 1024   # 原始资金为1024万元
list_1=[True,False]
cnt = 0
n=10
time_stamp = datetime.datetime.now()
print('run start time_stamp' + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))   #strftime可以自定义时间的输出格式，输出为time_stamp       2017.02.19-14:03:20
for x in range(0,1000):
    money = 1024
    cnt = 0
    n = 10
    while money > 1:
        cnt+=1
        if money > 10:           
            #choice=random.choice(list_1)
            choice = p_random(['B', 'S', 'M'],[105/216,105/216,6/216])
            if choice == 'B' :
                money = money + n
                n=10
            else:
                money = money - n
                n*=2
                if n > money:
                    n = money
        if money <= 10 or money > 2048:
            print("%12d\t%12d\t%12d\t"%(x,cnt,money))
            break   

time_stamp = datetime.datetime.now()
print('run over time_stamp' + time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))




