n=int(input('Введите натуральное число '))
b=n%8
n=n//8
a=n%8
n=n//8
delta=a-b
while n!=0:
    b=a
    a=n%10
    n=n//10
    if delta*(a-b)<=0:
        print('Цифры восьмеричной записи даннного числа не представляют строго монотонную последовательность')
        break
if delta*(a-b)>0:
    print('Цифры восьмеричной записи даннного числа представляют строго монотонную последовательность')
    
