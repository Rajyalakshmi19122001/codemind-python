n=int(input())
x=list(map(int,input().split()))
for i in range(n):
    if x[i]%2==0 and i%2==1:
        print(False)
        break
else:
    print(True)