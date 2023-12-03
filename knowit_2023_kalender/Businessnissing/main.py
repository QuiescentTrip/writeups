import math

file_path = 'knowit_2023_kalender\Businessnissing\input.txt'
money = 200000

try:
    with open(file_path, 'r') as file:
        file = file.read().split('\n')
        
    for i, day in enumerate(file):  
        
        stock = 0
        min_price = int(day.split(',')[0])
        max_profit = 0
        saved_min = 0
        
        for stock in day.split(','):
            stock = int(stock)
            if min_price == stock:
                continue
            if min_price > stock:
                min_price = stock
            elif max_profit < stock - min_price:
                max_profit = stock - min_price
                saved_min = min_price
        
        min_price = saved_min
        max_price = min_price + max_profit

        stock = math.floor(money / min_price)
        money = money % min_price
        money += stock * max_price
        
except FileNotFoundError:
    print("file not found")
    
print(money)