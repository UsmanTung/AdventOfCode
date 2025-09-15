from collections import defaultdict

def checkRules(rules, input):
    sum = 0
    for ordering in input:
        present = set(ordering)
        seen = set()
        sum+= ordering[len(ordering)//2]
        valid = True
        for val in ordering:
            for r in rules[val]:
                if r in present and r not in seen:
                    sum-=ordering[len(ordering)//2]
                    valid = False
                    break
            if not valid:
                break
            seen.add(val)
    return sum


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