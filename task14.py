a=int(input('Введите натуральное число: '))
b=a-1
while a%b>0:
    b=b-1
print('Наибольшим нетривиальным делителем числа',a,'является число',b)
