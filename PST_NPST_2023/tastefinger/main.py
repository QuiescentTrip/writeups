kode = "7-4 9-3 7-4 8-1 3-2 6-1 0-1 4-3 6-2 3-3 4-3 7-4 3-2 7-3 8-1 0-1 4-1 7-3 8-2 6-2 5-2 3-2 7-3 0-1 4-3 6-2 2-3 6-3 6-1 4-3 6-2 4-1"
kode_liste = kode.split(" ")
output = ""

phone = {
    0: "+",
    2: "ABC",
    3: "DEF",
    4: "GHI",
    5: "JKL",
    6: "MNO",
    7: "PQRS",
    8: "TUV",
    9: "WXYZ"
}

for string in kode_liste:
    a, b = string.split("-")
    første_tall = int(a)
    andre_tall = int(b)
    output += phone.get(første_tall)[andre_tall-1]

print("PST{" + " ".join(output.lower().split("+")) + "}")
    
     