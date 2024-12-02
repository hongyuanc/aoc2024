def read_file(content):
    safe = 0
    with open(content, 'r') as f:
        for line in f:
            nums = [int(x) for x in line.strip().split()]
            if analyse(nums):
                safe += 1

    return safe

def main():
    filename = "data/day2p1.txt"
    result = read_file(filename)

    print(result)

def analyse(nums):
    if is_valid_sequence(nums):
        return True
    
    for i in range(len(nums)):
        test_sequence = nums[:i] + nums[i+1:]
        if is_valid_sequence(test_sequence):
            return True
    
    return False

def is_valid_sequence(nums):
    differences = []
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        differences.append(diff)
        
        if abs(diff) < 1 or abs(diff) > 3:
            return False
            
    if any(diff > 0 for diff in differences) and any(diff < 0 for diff in differences):
        return False
        
    return True

if __name__ == "__main__":
    main()