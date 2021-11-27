time=int(input('Ввведите время в секундах: '))
#Решение делал сам подбором. не работает только с днями тут нужно было еще посидеть но 5 часов и так перебор
a=time//86400
if time > 86400:
    b=(time/86400-a)//24
    c=(time%86400-a)//60
    d= time%60
else:
    if time >7200:
        b=time//3600
        c=(time%3600-b)//60
        d=time%60
    else:
        if time > 3600:
            b=time//3600
            c=(time%3600)//60
            d=(time-c*60)-3600
        else:
            b=time//3600
            c=time//60
            d=(time-c*60)

print(a,b,c,d)

#Вот до этого я наверное не додумался бы от слова совсем))

duration = int(input('Введите время в секундах: '))
timepiece = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]

print(f'duration = {duration} сек\n{timepiece[0]} дн {timepiece[1]} час {timepiece[2]} мин {timepiece[3]} сек')