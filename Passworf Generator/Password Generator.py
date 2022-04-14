import random
import getpass
print("Passward should contain 5 number(from 0-9) and only number, there should no special charachter and space")
passward= getpass.gitpass("Creat Passward Here ")
if len(passward)==5:
    number=random.randint(0,5)
    list_number=[]
    k=''
    terminator=0
    while terminator==0:
        for i in range(5):
            number=random.randint(0,9)
            list_number.append(str(number))
        for i in list_number:
            k=k+i
        #print(k)
        if k==passward:
            print(f"Your Password is {k}")
            terminator=7
        else:
            k=''
            list_number = []