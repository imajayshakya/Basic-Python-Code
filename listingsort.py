def Selection_Sort(My_List):
    #i - outer Loop
    #j - inner Loop
    #k - index of the smaller element
    for i in range(len(My_List)-1):
        k=i    #i is the element assumed to be smallest
        for j in range(i+1,len(My_List)):
            if (My_List[j]<My_List[k]):
                k=j
        if(k!=1):
            temp=My_List[i]
            My_List[i]=My_List[k]
            My_List[k]=temp
My_List=[12,34,2,7,45,90,89,9,1]
print('Elements before sorting : ')
print(My_List)
Selection_Sort(My_List)
print('Elements after sorting in the List : ')
print(My_List)