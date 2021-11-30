my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_new_message = []

for i in my_list:
    if i.replace('+', '').replace('-', '').isdigit():
        if i.isdigit():
            my_new_message.append(f'"{int(i):02}"')
        else:
            my_new_message.append(f'"{i[0]}{int(i[1:]):02}"')
    else:
        my_new_message.append(i)
print(' '.join(my_new_message))

# Сделано интересно. Но пришлось почитерить немного так как самому тяжеловато было.






