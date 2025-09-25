def sumOfAll(input):
    seen = set()
    result = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            visited = set()
            if (i,j) not in seen:
                area, visited = getIsland(input, i, j, visited)
                area += 1
                #perimeter = getPerimeter(visited)
                temp = set()
                sides = getSides(visited, temp)
                for (x, y) in visited:
                    seen.add((x, y))
                result += area * sides
    return result

def getSides(coords):
    sides = 0
    for (i, j) in coords:
        U = (i-1, j) in coords
        D = (i+1, j) in coords
        L = (i, j-1) in coords
        R = (i, j+1) in coords

        if not U and not L: sides += 1
        if not U and not R: sides += 1
        if not D and not L: sides += 1
        if not D and not R: sides += 1

        if U and L and (i-1, j-1) not in coords: sides += 1
        if U and R and (i-1, j+1) not in coords: sides += 1
        if D and L and (i+1, j-1) not in coords: sides += 1
        if D and R and (i+1, j+1) not in coords: sides += 1
    return sides



def getPerimeter(visited):
    perimeter = 0
    for (i,j) in visited:
        temp = 4
        if (i+1, j) in visited:
            temp -= 1
        if (i-1, j) in visited:
            temp -= 1
        if (i, j+1) in visited:
            temp -= 1
        if (i, j-1) in visited:
            temp -= 1
        perimeter += temp
    return perimeter


def getIsland(input, i ,j, visited):               
    if i < 0 or i >= len(input) or j < 0 or j >= len(input[0]) or (i,j) in visited:
        return (0, visited)
    visited.add((i,j))
    sum = 0
    if i + 1 < len(input) and input[i][j] == input[i+1][j] and (i+1,j) not in visited:
        sum += 1 + getIsland(input, i+1, j, visited)[0]
    if j + 1 < len(input) and input[i][j] == input[i][j+1] and (i,j+1) not in visited:
        sum += 1 + getIsland(input, i, j+1, visited)[0]
    if i - 1 >= 0 and input[i][j] == input[i-1][j] and (i-1,j) not in visited:
        sum += 1 + getIsland(input, i-1, j, visited)[0]
    if j - 1 >=0  and input[i][j] == input[i][j-1] and (i,j-1) not in visited:
        sum += 1 + getIsland(input, i, j-1, visited)[0]
    return (sum, visited)

def main():
    input = []
    with open('input.txt', 'r') as file:
        temp = []
        for line in file:
            temp = [c for c in line.strip()]
            input.append(temp)
    #print(input)
    print(f"sum of all : {sumOfAll(input)}")

if __name__ == "__main__":
    main()