def sum_odd_even():
    my_list=[]
    sum_even = 0
    sum_odd = 0
    p=int(input("how many numbers do you want to compute:"))
    for x in range(p):
        n=int (input("enter number :"))
        my_list.append(n)
    for num in my_list:
        if num%2==0:
            sum_even+=num
        else:
            sum_odd+=num    
    my_tupple=(sum_even,sum_odd)       
    return my_tupple
answer=sum_odd_even()
print(answer) 