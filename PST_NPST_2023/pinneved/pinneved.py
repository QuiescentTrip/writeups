"""TEMMELIG HEMMELIG"""
"""SÃ¸r-Polar Sikkerhetstjeneste"""
"""HÃ¸yeksplosivt script for tilintetgjÃ¸relse av Julenissens slede"""


otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

def explode(input, antall):
    storrelse = len(input) // antall
    fragmenter = []
    
    for i in range(0, len(input), storrelse):
        fragment = input[i:i+storrelse]
        fragmenter.append(fragment)
    
    return fragmenter

slede = "asdfasdfasdfasdfasdfasdfasdfasdf"

bang = explode(slede, 24)
eksplosjon = [''.join([chr(ord(c) + 2) for c in fragment]) for fragment in bang]
print(eksplosjon)
pinneved = [str(eksplosjon[i]) for i in reversed(otp)]

print(''.join(pinneved))