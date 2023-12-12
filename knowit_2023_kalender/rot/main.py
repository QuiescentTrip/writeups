crypt = "Ojfkyezkz bvclae zisj a guomiwly qr tmuematbcqxqv sa zmcgloz."

def is_2(i):
    binary = bin(i)[2:]
    count = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            count += 1
    return count % 2 == 0

list = []
for i in range(1,10000):
    if is_2(i):
        list.append(i)
    

def rot_alpha(n):
    from string import ascii_lowercase as lc, ascii_uppercase as uc
    lookup = str.maketrans(lc + uc, lc[n:] + lc[:n] + uc[n:] + uc[:n])
    return lambda s: s.translate(lookup)

output = ""

x = 666
for i, char in enumerate(crypt):
    y = list[i]
    n = x * y % 13
    print(n)
    output += rot_alpha(n)(char)
    

print(crypt)
print(output)