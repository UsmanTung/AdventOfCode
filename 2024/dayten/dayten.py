def trailSum(input):
    zeroCoords = []
    result = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "0":
                zeroCoords.append((i,j))

    def dfs(i, j, nines):
        if input[i][j] == "9":
            nines.append((i,j))
            return 
        if i-1>=0 and input[i-1][j] == str(int(input[i][j]) + 1):
            dfs(i-1,j, nines)
        if j-1>=0 and input[i][j-1] == str(int(input[i][j]) + 1):
            dfs(i, j-1, nines)  
        if i+1 < len(input) and input[i+1][j] == str(int(input[i][j]) + 1):
            dfs(i+1, j, nines)
        if j+1 < len(input[0]) and input[i][j+1] == str(int(input[i][j]) + 1):
            dfs(i, j+1, nines)

    for (i,j) in zeroCoords:
        nines= []
        dfs(i, j, nines)
        result += len(nines)
    return result


def main():
    input = []
    with open('input.txt', 'r') as file:
        temp = []
        for line in file:
            strippedLine = line.strip()
            input.append(strippedLine)
    print(input)
    print(f"sum of trails: {trailSum(input)}")


if __name__ == "__main__":
    main()