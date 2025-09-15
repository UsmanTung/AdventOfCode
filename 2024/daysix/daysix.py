def locationsPatrolled(input, i, j):
    directions = [(-1,0), (0,1),(1,0),(0,-1)]
    seen = set()
    dirIndex = 0
    total = 1
    seen.add((i,j))
    while i+directions[dirIndex][0] >=0 and j+directions[dirIndex][1] >=0 and i+directions[dirIndex][0]<len(input) and j+directions[dirIndex][1] <len(input[0]):
        ni = i+directions[dirIndex][0]
        nj = j+directions[dirIndex][1]

        if input[ni][nj] == "#":
            dirIndex = (dirIndex+1)%4
            continue
        i,j= ni,nj
        if (i,j) not in seen:
            seen.add((i,j))
            total+=1
    return total

def main():
    with open('input.txt', 'r') as file:
        
        input = []
        for line in file:
            input.append(list(line.strip()))

    starti, startj = 0,0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "^":
                starti, startj = i, j

    print(f"locationsPatrolled : {locationsPatrolled(input,starti, startj)}")

if __name__ == "__main__":
    main()