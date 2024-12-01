def read_lists_from_file(filename):
    list1 = []
    list2 = []
    
    with open(filename, 'r') as f:
        for line in f:
            nums = line.strip().split()
            if len(nums) == 2:
                list1.append(int(nums[0]))
                list2.append(int(nums[1]))
    
    return list1, list2

def calculate_total_distance(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    
    total_distance = 0
    for num1, num2 in zip(sorted_list1, sorted_list2):
        distance = abs(num1 - num2)
        total_distance += distance
    
    return total_distance

def main():
        filename = "data/day1p1.txt"
        list1, list2 = read_lists_from_file(filename)
        
        if not list1 or not list2:
            raise ValueError("No valid number pairs found in the file")
        
        if len(list1) != len(list2):
            raise ValueError("Lists must be of equal length")
        
        result = calculate_total_distance(list1, list2)
        print(f"Total distance between the lists: {result}")

if __name__ == "__main__":
    main()