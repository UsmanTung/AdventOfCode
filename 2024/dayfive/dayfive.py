from collections import defaultdict

def checkRules(rules, input):
    sum = 0
    for ordering in input:
        present = set(ordering)
        seen = set()
        valid = True
        for val in ordering:
            for r in rules[val]:
                if r in present and r not in seen:
                    sum+=reorder(ordering, rules)
                    valid = False
                    break
            if not valid:
                break
            seen.add(val)
    return sum

def reorder(ordering, rules):
    present = set(ordering)
    valid = True
    newOrdering = []
    while ordering:
        valid = True
        for r in rules[ordering[0]]:
            if valid and r in present and r not in set(newOrdering):
                ordering.append(ordering.pop(0))
                valid = False
                break
        if valid:
            newOrdering.append(ordering.pop(0))
    return newOrdering[len(newOrdering)//2]
    


def main():
    rules = defaultdict(list)
    input = []
    with open('input.txt', 'r') as file:
        ruleLines = True
        for line in file:
            if line == "\n":
                ruleLines = False
            elif ruleLines:
                a, b = line.split("|")
                rules[int(b)].append(int(a))
            else:
                line.strip()
                ordering = [int(x) for x in line.split(",")]
                input.append(ordering)
    
    print(f"checkRules sum : {checkRules(rules, input)}")

if __name__ == "__main__":
    main()