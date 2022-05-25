N=int(input())
l=list(map(int,input().split()))
d=[]
e=[]
c=0
for i in l:
  if i in d:
      continue
  d.append(i)
print(sum(d))