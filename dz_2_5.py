prices = [57.98, 33.15, 77, 97.8, 179.79, 44.17, 59.69, 12.9, 100, 131.1]
for i in prices:
    rub, cop = f'{i:.02f}'.split('.')
    print(f' Цена: {rub} руб {cop} копп')

# B

print(f'id started: {id(prices)}-{prices}')
prices.sort()
print(f'id changed: {id(prices)}-{prices}')

#C-D

new_list = sorted(prices, reverse=True)
print(f'id changed: {id(new_list)}-{new_list}\n{new_list[:5][::-1]}')

# Пятое задание сам не делал перенес с урока
