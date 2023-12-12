import math
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_twin_primes(start, end):
    count = 0
    for num in range(start, end + 1):
        if is_prime(num) and is_prime(num + 2):
            count += 1
    return count

start_range = 0
end_range = 46656 + 666

twin_primes_count = count_twin_primes(start_range, end_range)
print(twin_primes_count)