crypt = "Ojfkyezkz bvclae zisj a guomiwly qr tmuematbcqxqv sa zmcgloz."
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

def is_2(i):
    binary = bin(i)[2:]
    return [*binary].count('1') % 2 == 0

list = []
for i in range(len(crypt) * 2):
    if is_2(i):
        list.append(i)
    

def rot_alpha(n, char):
    if char.isalpha():
        return alphabet[(alphabet.index(char) + n) % len(alphabet)]
    else:
        return char

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


output = ""
x = count_twin_primes(6**6 + 666)
crypt = [*crypt]
for i, char in enumerate(crypt):
    y = list[i]
    n = x * y 
    crypt[i] = rot_alpha(-n, char)

print("".join(crypt))