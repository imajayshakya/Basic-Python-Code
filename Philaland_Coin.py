testcases = int(input())
for i in range(1,testcases+1):
    price = int(input())
    count = 0
    while price >= 1:
        price = price // 2
        count = count + 1
    print(count)