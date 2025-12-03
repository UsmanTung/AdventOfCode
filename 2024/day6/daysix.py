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

def findAllLoops(input, si, sj):
    directions = [(-1,0), (0,1),(1,0),(0,-1)]
    total = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            currI, currJ = si,sj
            if input[i][j] == "#" or input[i][j]== "^":
                continue
            temp= input[i][j]
            input[i][j] = "#"
            dirIndex = 0
            seen = set()
            seen.add((currI, currJ, dirIndex))
            while currI+directions[dirIndex][0] >=0 and currJ+directions[dirIndex][1] >=0 and currI+directions[dirIndex][0]<len(input) and currJ+directions[dirIndex][1] <len(input[0]):
                ni = currI+directions[dirIndex][0]
                nj = currJ+directions[dirIndex][1]
            

                if input[ni][nj] == "#":
                    dirIndex = (dirIndex+1)%4
                    continue    
                currI,currJ = ni,nj
                if (currI, currJ, dirIndex) in seen:
                    total+=1
                    break
                seen.add((currI,currJ,dirIndex))
            input[i][j] = temp
                
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
    print(f"totalLoops possible : {findAllLoops(input, starti ,startj)}")

if __name__ == "__main__":
    main()