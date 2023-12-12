file = 'AoC2023\Cube_Conundrum\input.txt'
# 12 red cubes, 13 green cubes, and 14 blue cubes.
colors = ['red', 'green', 'blue']

with open('file', 'r') as file:
    games = file.read().split('\n')
    for i, game in enumerate(games):
        i += 1
        red, green, blue = 0
        for match in game:
            match = match.split(':')[0].split(',')
            for color in game:
                if color in colors:
                    
            
