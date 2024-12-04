content = "data/day4.txt"
text = []

with open(content, 'r') as file:
    for line in file:
        text.append(line.strip())

def find_xmas_pattern(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    def check_diagonal_mas(row, col, dr, dc):
        if not (0 <= row < rows and 0 <= col < cols and 
                0 <= row + 2*dr < rows and 0 <= col + 2*dc < cols):
            return False
            
        chars = [
            grid[row][col],
            grid[row + dr][col + dc],
            grid[row + 2*dr][col + 2*dc]
        ]
        return ''.join(chars) in ['MAS', 'SAM']

    for i in range(1, rows-1):  # Avoid edges since we need space for the pattern
        for j in range(1, cols-1):
            if grid[i][j] == 'A':  # Center must be 'A'
     
                if ((check_diagonal_mas(i-1, j-1, 1, 1) and 
                     check_diagonal_mas(i-1, j+1, 1, -1)) or  
                    (check_diagonal_mas(i+1, j-1, -1, 1) and 
                     check_diagonal_mas(i+1, j+1, -1, -1))):
                    count += 1
                    
    return count

def main():
    print(find_xmas_pattern(text))

if __name__ == "__main__":
    main()