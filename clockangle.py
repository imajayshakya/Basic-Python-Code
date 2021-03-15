N=int(input())
L=float(input())
UTC=0
Ti=((N/360)*L)*60
Time= int(Ti//60) 
ji=int(Ti-((Ti//60)*60))
#IST=print("{}{}{}".format(Time,":",ji))
def clockangle(hour, minute):
    ans = abs((hour * 30 + minute * 0.5) - (minute * 6))
    return min(360-ans,ans)
Ans=clockangle(Time,ji)
print("%0.2f" %Ans)