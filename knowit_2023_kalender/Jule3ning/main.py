data = [int(x) for x in open("knowit_2023_kalender\Jule3ning\push.txt", 'r').read().split(",")]

output = []
saved = [0]
down = False

for i, pushup in enumerate(data):
    if saved[-1] > pushup:
        down = True
        
    if down:
        if saved[-1] < pushup:
            saved = [0]
            saved.append(data[i-1])
            down = False
            
    if len(saved) > len(output):
        output = saved
    saved.append(pushup)
    
print(sum(output) if len(output) > len(saved) else sum(saved))
