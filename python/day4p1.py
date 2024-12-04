content = "data/day4.txt"
text = []

with open(content, 'r') as file:
    for line in file:
        text.append(line.strip())

def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    
    def check_direction(row, col, dx, dy):
        if not (0 <= row + 3*dx < rows and 0 <= col + 3*dy < cols):
            return False
        return (grid[row][col] == 'X' and 
                grid[row + dx][col + dy] == 'M' and
                grid[row + 2*dx][col + 2*dy] == 'A' and
                grid[row + 3*dx][col + 3*dy] == 'S')
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if check_direction(i, j, dx, dy):
                    count += 1
    
    return count

def main():
    print(find_xmas(text))

if __name__ == "__main__":
    main()