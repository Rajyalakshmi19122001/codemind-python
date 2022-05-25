N=int(input())
l=list(map(int,input().split()))
d=[]
c=[]
for i in l:
  if i in d:
      continue
  d.append(i)
for j in d:
    c.append(j)
    c.append(l.count(j))
print(*c)