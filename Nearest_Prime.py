t=int(input())
for _ in range(t):
    n=int(input())
    next_prime=n
    while True:
        fc=0
        for i in range(1,next_prime+1):
            if next_prime%i==0:
                fc+=1
        if fc==2:
            break
        next_prime+=1
    prev_prime=n
    while True:
        fc=0
        for i in range(1,prev_prime+1):
            if prev_prime%i==0:
                fc+=1
        if fc==2:
            break
        prev_prime-=1
    if n-prev_prime<=next_prime-n:
        print(prev_prime)
    else:
        print(next_prime)
    