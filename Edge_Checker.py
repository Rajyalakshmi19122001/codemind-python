a,b=map(int,input().split())
c=a+1
d=a-1
if b==c or b==d:
    print("Yes")
elif a==10 and b==1:
    print("Yes")
elif a==1 and b==10:
    print("Yes")
else:
    print("No")
