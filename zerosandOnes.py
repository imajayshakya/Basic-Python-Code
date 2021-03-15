L1=list(map(int,input().strip().split()))
def ZerosAndones(List1) : 
    a = 0 
    for i in range(0, len(List1)) : 
        if (List1[i] == 0) : 
            a+=1
    for i in range(0, a) : 
        List1[i] = 0
    for i in range(a, len(List1)) : 
        List1[i] = 1
          
def Zeroprint(List1) :
    for i in range(0,len(List1)) : 
        print(List1[i] , end = " ")

ZerosAndones(L1)
Zeroprint(L1)