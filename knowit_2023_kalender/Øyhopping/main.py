def countIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    islands = 0

    def exploreIsland(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] != 'X':
            return
        
        grid[x][y] = '.'  # Mark the visited cell
        exploreIsland(x+1, y)  # Explore right cell
        exploreIsland(x-1, y)  # Explore left cell
        exploreIsland(x, y+1)  # Explore upper cell
        exploreIsland(x, y-1)  # Explore lower cell
        exploreIsland(x+1, y+1)
        exploreIsland(x-1, y-1)
        exploreIsland(x-1, y+1)
        exploreIsland(x+1, y-1)
        
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                exploreIsland(i, j)
                islands += 1

    return islands

with open('knowit_2023_kalender\Øyhopping\kart.txt', 'r') as file:
    kart = [list(line.strip()) for line in file.readlines()]

print(len(kart))
print(countIslands(kart))
