file_path = 'knowit_2023_kalender/Jule-en/reps.txt'

saved = []
final = []

with open(file_path, 'r') as file:    
    file = file.read().split(',')
    
    for okt in file:
        okt = int(okt)
        # if saved sånn at vi ikke får index out of bounds
        if saved and saved[-1] > okt:
            if len(final) < len(saved):
                final = saved
            saved = []
        saved.append(okt)

print(sum(final))
    