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

def calculate_similarity_score(list1, list2):
    total_score = 0
    
    right_freq = {}
    for num in list2:
        right_freq[num] = right_freq.get(num, 0) + 1
    
    for num in list1:
        count_in_right = right_freq.get(num, 0)

        score_contribution = num * count_in_right
        total_score += score_contribution
    
    return total_score

def main():
    filename = "data/day1p1.txt"
    list1, list2 = read_lists_from_file(filename)
    
    if not list1 or not list2:
        raise ValueError("No valid number pairs found in the file")
    
    print(f"Number of pairs read: {len(list1)}")
    
    similarity_score = calculate_similarity_score(list1, list2)
    print(f"\nFinal similarity score: {similarity_score}")
    
if __name__ == "__main__":
    main()