l=int(input('Введите члены последовательности:\n'))
if l!=0:
    m=int(input())
else:
    print('Последовательность не пилообразная') 
if m!=0:
    r=int(input())
else:
    print('Последовательность не пилообразная')
if r==0:
    print('Последовательность не пилообразная')
    raise SystemExit
while r!=0:
    if (l-m)*(r-m)<=0:
        print('Последовательность не пилообразная')
        break
    l=m
    m=r
    r=int(input())
if r==0:
    r=l
    if (l-m)*(r-m)>0:
        print('Последовательность пилообразная')
    else:
        print('Последовательность не пилообразная')
