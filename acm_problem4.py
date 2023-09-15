def generateFibino(num):
    prev = 0
    curr = 1
    sum = 0
    while True:
        next = prev + curr
        if next > num:
            break
        if next%2 == 0:
            sum = sum + next
        prev = curr
        curr = next
    return sum
   
n = int(input('Enter number of test cases:'))
if n >= 1 and n <= pow(10, 5):
    numbers=[]
    for i in range(n):
        num = int(input())
        if num >= 10 and num <= (4 * pow(10,16)) :
            numbers.append(num)
        else:
            print('Wrong input')
    for j in numbers:
        print(generateFibino(j))
else:
    print('Wrong test case count')