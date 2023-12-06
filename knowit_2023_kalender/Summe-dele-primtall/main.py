from sympy import isprime

limit = 100000000
count = 0
for num in range(1, limit + 1):
    digit_sum = sum(map(int, str(num)))
    slash = num / digit_sum
    if slash.is_integer():
        if isprime(int(slash)):
            count+=1
print(count)
