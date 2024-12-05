def read(content):
    rules_data = []
    updates_data = []
    change = False
    with open(content, 'r') as file:
        for line in file:
            if line.strip() == '':
                change = True
                continue
            if change:
                updates_data.append([int(x) for x in line.strip().split(',')])
            else:
                parts = line.strip().split('|')
                rules_data.append([int(parts[0]), int(parts[1])])
    return rules_data, updates_data

def process_rules(data):
    rules = {}
    for row in data:
        key = row[0]
        value = row[1]
        if key not in rules:
            rules[key] = [value]
        else:
            rules[key].append(value)
    return rules

def check_rule_violation(pages, rules):
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            page1, page2 = pages[i], pages[j]
            if page2 in rules and page1 in rules[page2]:
                return True
    return False

def check_correct(updates, rules_dict):
    correct_updates = []
    for update in updates:
        if not check_rule_violation(update, rules_dict):
            correct_updates.append(update)
    return correct_updates

def get_middle_sum(correct_updates):
    total = 0
    for update in correct_updates:
        mid = len(update) // 2
        total += update[mid]
    return total

def main():
    rules_data, updates_data = read('data/day5.txt')
    rules_dict = process_rules(rules_data)
    correct_updates = check_correct(updates_data, rules_dict)
    result = get_middle_sum(correct_updates)
    print(result)

if __name__ == "__main__":
    main()