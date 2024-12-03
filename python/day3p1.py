import re

def process_corrupted_memory(text):
    # Pattern to match mul(X,Y) where X and Y are 1-3 digit numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all valid matches
    matches = re.finditer(pattern, text)
    
    total = 0
    results = []
    
    for match in matches:
        x = int(match.group(1))
        y = int(match.group(2))
        result = x * y
        results.append((x, y, result))
        total += result
    
    return total

def main():
    with open('data/day3p1.txt', 'r') as file:
        content = file.read()
        result = process_corrupted_memory(content)
        print(result)

if __name__ == "__main__":
    main()