def countAntinodes(input):
    totalSum = 0
    seen = set()
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                totalSum+=checkForSameNode(input, i ,j, seen)
    output = [["." for _ in range(len(input[0]))] for _ in range(len(input))]
    for (i, j) in seen:
        output[i][j] = "#"
    prettyPrint(output)
    return totalSum

def checkForSameNode(input, i ,j, seen):
    if i == 9 and j == 9:
        print("here")
    innerSum = 0
    for x in range(len(input)):
        for y in range(len(input[0])):
            if input[x][y] == input[i][j] and (x!=i or y!=j):
                i2 = x-i
                j2 = y-j
                if (x,y) not in seen:
                    seen.add((x,y))
                    innerSum+=1
                while x+i2 >=0 and x+i2 < len(input) and y+j2 >= 0 and y+j2 < len(input[0]):
                    if (x+i2, y+j2) not in seen:
                        innerSum += 1
                    x+=i2
                    y+=j2
                    seen.add((x, y))
                    
    return innerSum

def main():
    input = []
    with open('input.txt', 'r') as file:
        for line in file:
            newLine = line.strip()
            temp = []
            for c in newLine:
                temp.append(c)
            input.append(temp)
    print(f"total antinodes : {countAntinodes(input)}")

def prettyPrint(input):
    for i in range(len(input)):
        for j in range(len(input[0])):
            print(input[i][j], end="")
        print("\n")

if __name__ == "__main__":
    main()


# 1 2 and 2 1 means there should be at 0 3 and 3 0
# i j and x y              i-abs(x-i) 