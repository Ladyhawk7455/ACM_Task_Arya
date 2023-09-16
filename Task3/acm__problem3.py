def multiple(m):
    sum=0
    for i in range(1,m):
        if i%3==0 or i%5==0:
            sum=sum+i
    return sum

t=int(input("Enter number of test cases:"))
if t>=1 and t<=pow(10,5):
    numbers=[]
    for i in range(t):
        n=int(input())
        if n >= 10 and n <= pow(10,9) :
            numbers.append(n)
        else:
            print('Wrong input')
    for j in numbers:
        print(multiple(j))
else:
    print('Wrong test case count')
