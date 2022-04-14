import random
from time import sleep
name=input()
my_name=''
x=[]
times=0
flag=1
while flag==1:

    for i in range(0,len(name)):
        x.append(name[random.randint(0,len(name)-1)])

    for i in x:
        my_name=my_name+i
    #sleep(0.01)
    times=times+1
    print(times, my_name)
    if my_name==name:
        flag=4
        break
    else:
        my_name=''
        x=[]
print(my_name)
print(f"After {times} your name came ")
