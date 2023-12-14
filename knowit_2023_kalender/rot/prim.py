def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_twin_primes(end):
    count = 0
    for num in range(0, end + 1):
        if is_prime(num) and is_prime(num + 2):
            count += 1
    return count

x = count_twin_primes(6**6 + 666)
print(x)