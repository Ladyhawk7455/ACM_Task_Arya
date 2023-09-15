def isPrime(x):
    h=0
    for g in range(2,(x//2)+1):
        if x%g == 0:
            h=h+1
    return h
   
def getHighestPrimeFactor(num):
    factor = 0  
    for v in range(2,num+1):
        if num%v == 0 and isPrime(v) == 0:
            factor=v
    return factor
   
n = int(input('Enter number of test cases:'))
if n>=1 and n<=10:
    numbers=[]
    for i in range(n):
        num=int(input())
        if num>=10 and num<= pow(10,12):
            numbers.append(num)
        else:
            print('Wrong input.')
    for j in numbers:
        print(getHighestPrimeFactor(j))
else:
    print('Wrong input.')
