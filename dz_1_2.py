a=[i**3 for i in range(1,1000,2)]#формулу нашел в гугле так как в куб через циклы не понимаю как возвести
sum=0
for ind,val in enumerate(a):#дальше решение не мое воспроизвел в ручную с чата
    sum_diggits=0
    while val>0:
        sum_diggits=sum_diggits+val%10
        val=val//10
    if sum_diggits%7==0:
        sum=sum+a[ind]
print(sum)
print(a)
sum1=0
for i,val in enumerate(a):#выполнил по примеру с урока
    a[i]+=17
for i,val in enumerate(a):#повторил предидущий цикл
    sum_diggits2=0
    while val>0:
        sum_diggits2=sum_diggits2+val%10
        val=val//10
    if sum_diggits2%7==0:
        sum1=sum1+a[i]
print(sum1)
print(a)






