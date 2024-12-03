import re

def process_corrupted_memory(text):
    # Patterns for all instructions
    mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    do_pattern = r'do\(\)'
    dont_pattern = r'don\'t\(\)'
    
    # Find all instructions with their positions
    instructions = []
    
    # Find multiplications
    for match in re.finditer(mul_pattern, text):
        x = int(match.group(1))
        y = int(match.group(2))
        instructions.append(('mul', match.start(), x, y))
    
    for match in re.finditer(do_pattern, text):
        instructions.append(('do', match.start(), None, None))
    
    # Find don't() instructions
    for match in re.finditer(dont_pattern, text):
        instructions.append(('dont', match.start(), None, None))
    
    instructions.sort(key=lambda x: x[1])
    
    # Process instructions in order
    enabled = True 
    total = 0
    
    for inst_type, pos, x, y in instructions:
        if inst_type == 'do':
            enabled = True
        elif inst_type == 'dont':
            enabled = False
        elif inst_type == 'mul' and enabled:
            result = x * y
            total += result
            
    return total

def main():
    with open('data/day3p1.txt', 'r') as file:
        content = file.read()
        result = process_corrupted_memory(content)
        print(result)

if __name__ == "__main__":
    main()