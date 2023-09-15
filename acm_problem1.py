lst=[]
sum=0
x=int(input('How many numbers do you want to be in your list:'))
if len(lst) <= 100:
    for i in range(x):
        num=int(input())
        lst.append(num)
    for j in lst:
        if j%2 != 0:
            sum=sum+j
else:
    print('Wrong input')
print(sum)
            

