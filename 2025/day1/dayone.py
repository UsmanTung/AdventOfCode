def sumZeroes(data):
    total = 0
    curr = 50
    for line in data:
        if line[0] == "L":
            curr -= int(line[1:])
            curr %= 100
        else:
            curr += int(line[1:])
            curr %= 100
        if curr == 0:
            total += 1
    return total

def main():
    with open("2025/day1/input.txt") as f:
        data = f.read().strip().split("\n")

    print(sumZeroes(data))
    

if __name__=="__main__":
    main()

    