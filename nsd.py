import sys, math
import time
start = time.time()
sys.stdin = open('gcdarray.in','r')
sys.stdout = open('gcdarray.out','w')
def nsd(a):
    res=0
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            res+=a[i]-a[i+1]
            a[i+1]=a[i]
    #print(a)
    min_res=999
    for i in [2]+list(range(3,max(a)+1,2)):
        temp_res=0
        for j in range(len(a)):
            #print("i=",i,"j=",a[j])
            if a[j]%i!=0:
                temp_res+=int(a[j]/i+0.99999)*i-a[j]
                #print("int=",int(a[j]/i+0.99999)*i)
        if temp_res<min_res:
            min_res=temp_res
            #print(i)
        #print(i, temp_res)
    print(min_res+res)

t=int(input())
for z in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    nsd(a)
print('It took', time.time()-start, 'seconds.')