N=int(input())
num=1
for i in range(1,N+1,1):
    p=i
    for j in range(1,i+1,1):
        print(p,end=" ")
        p=p+5-j
    print()