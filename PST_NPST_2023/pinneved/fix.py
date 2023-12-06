# Read the transformed text from the file
with open("PST_NPST_2023/pinneved/pinneved.txt", "r") as file:
    encrypted_text = file.read()
# Given encrypted text and 'otp' list
otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

def explode(input, antall):
    size = len(input) // antall
    fragments = []
    
    for i in range(0, len(input), size):
        fragment = input[i:i+size]
        fragments.append(fragment)
    
    return fragments

original_order = list(reversed(range(len(otp))))
def reverse_shift(s):
    return ''.join([chr(ord(c) - 2) for c in s])

fragments = explode(encrypted_text, 24)

decrypted_fragments = [''.join([chr(ord(c) - 2) for c in fragment]) for fragment in fragments]

thing = [13,9,12,17,23]
for i in range(0,24):
    if '/' in decrypted_fragments[i]:
        print(i)
        

for i in thing:
    print(decrypted_fragments[i])
