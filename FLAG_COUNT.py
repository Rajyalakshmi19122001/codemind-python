n=int(input())
arr=[]
fa=fb=2
fn=0
for i in range(n):
    arr.append(fa)
    fn=fa+fb
    fa=fb
    fb=fn
print(arr[n-1])