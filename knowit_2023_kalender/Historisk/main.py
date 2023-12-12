import time
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'ø', 'å']
with open('knowit_2023_kalender\Historisk\cypher.txt', 'r', encoding='utf-8') as file:
    cypher = file.read().replace('\n', " ").split(" ")
with open('knowit_2023_kalender\Historisk\input.txt', 'r') as file:
    input = file.read().split('\n')
print(len(input))

final = ""
for i, thing in enumerate(input):
    num_list = [int(num) for num in thing.strip('[]').split(', ')]
    dict = {}
    
    for j, num in enumerate(num_list):
        dict.update({alphabet[num] : alphabet[j]})
    
    for char in cypher[i]:
        if char in alphabet:
            final += dict[char]
    
    final += " "
print(final)