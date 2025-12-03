from collections import Counter

def afterXBlinks(blinks, input):
    unique = Counter(input)
    for i in range(blinks):
        count = Counter()
        for val, c in unique.items():
            if val == "0":
                count["1"] += c
            elif len(val) % 2 == 0:
                middle = len(val) // 2
                left = val[0:middle]
                right = val[middle:len(val)]
                if int(right) == 0:
                    right = "0"
                else:
                    while right[0] == "0":
                        right = right[1:len(right)]
                count[left] += c
                count[right] += c
            else:
                count[str(int(val) * 2024)] += c
        unique = count
    return sum(unique.values())

def main():
    with open('input.txt', 'r') as file:
        input = file.read().split()
    print(f"after 25 Blinks :{afterXBlinks(25, input)}")
    print(f"after 75 Blinks :{afterXBlinks(75, input)}")
if __name__ == "__main__":
    main()