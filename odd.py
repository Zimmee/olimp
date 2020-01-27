import sys, math
sys.stdin = open('even-or-odd.in','r')
sys.stdout = open('even-or-odd.out','w')
n = int(input())
a = map(int, input().split())
def divide(n):
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i
    yield n
    
s=''  
for j in a:
    if j==1:
        s+='1'
    else:
        s+=divide(j)
print(s)