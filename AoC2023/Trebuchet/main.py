import re

output = 0
pattern = '[a-zA-Z]'
numbs = ['one', 'two','three','four','five','six','seven','eight','nine']

catches = {
    'twone' : '21',
    'oneight' : '18',
    'nineight' : '98',
    'eightwo' : '82',
    'eighthree' : '83',
    'fiveight' : '58',
    
}

with open('AoC2023\Trebuchet\input.txt', 'r') as file:
    content = file.read().split('\n')
    for line in content:
        for catch, value in catches.items():
            if catch in line:
                line = re.sub(catch, value, line)
                 
        for i, num in enumerate(numbs):
            line = re.sub(num, str(i+1), line)
        numbers = re.sub(pattern, "", line)
        fnl = ""
        if len(numbers) >= 1:
            fnl += numbers[0]
            if len(numbers) == 1:
                fnl += numbers[0]
        if len(numbers) >= 2:
            fnl += numbers[-1]
        if fnl != "":
            output += int(fnl)
            
            
print(output)