import sys, math
sys.stdin = open('room.in','r')
sys.stdout = open('room.out','w')
n,m,p = map(int, input().split())
p-=2*n+2*m
if (p-n*2)%2==0 and (p-n*2)/2<m and (p-n*2)/2>0:
    print("YES")
    print(n,int(m-(p-n*2)/2))
    print(1,int((p-n*2)/2))
    print(n-1,int((p-n*2)/2))
elif (p-m*2)%2==0 and (p-m*2)/2<n and (p-m*2)/2>0:
    print("YES")
    print(m,int(n-(p-m*2)/2))
    print(1,int((p-m*2)/2))
    print(m-1,int((p-m*2)/2))
else:
    print("NO")