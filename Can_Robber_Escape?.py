a=int(input())
l=list(map(int,input().split()))
f=0
for i in l:
    if i<a:
        f=1
    else:
        f=0
        break
if f==1:
    print("YES")
else:
    print("NO")