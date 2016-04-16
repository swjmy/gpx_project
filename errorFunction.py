#coding=utf-8
#求Ck的代码
'''
def Clist(k):
    if k==0:
        num=0
        return 1.0
    else:
        num=0.0
        for m in range(0,k):
            num+=(Clist(m)*Clist(k-1-m))/((m+1)*(2*m+1))
        return num
#print ("请输入k的值：")
k=15
result=Clist(k)
print result
'''


import math

funCMemo=[]
funCMemoFlag=[]
count = 0
def funC(k):
    if k!=0:
        sum=0
        if funCMemoFlag[k]==1:
            return funCMemo[k]
        global count
        count = count+1
        for i in range(k):
            sum=sum+(funC(i)*funC(k-1-i))/((i+1)*(2*i+1))
        funCMemoFlag[k]=1
        funCMemo[k]=sum
        return sum
    else:
        return 1.0

def funE(n,k):
    sum=0.0
    for i in range(k):
        sum+=funC(i)*(math.pow((math.sqrt(math.pi)*n/2),(2*i+1)))/(2*i+1)
    return sum

erf=0
for i in range(128):
    funCMemo.append(0)
    funCMemoFlag.append(0)
n_num=input("input n:\n") #输入n
k_num=input("input k:\n") #输入k
erf=funE(float(n_num),int(k_num))
print("erf={%f}\n"%(erf))
print("count={%d}\n"%(count))




































