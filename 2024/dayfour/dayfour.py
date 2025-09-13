def xmasSearch(input):
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "X":
                sum+= searchNext(i,j, input)
    return sum

def searchNext(i, j, input):
    return searchTop(i,j, input) + searchTopRight(i,j,input) + searchRight(i,j,input) + searchBottomRight(i,j,input) + searchBottom(i,j,input)+searchBottomLeft(i,j,input) +searchLeft(i,j,input) + searchTopLeft(i,j,input)
def searchTop(i,j, input):
    if i-3 >=0 and input[i-1][j] == "M" and input[i-2][j] == "A" and input[i-3][j] == "S":
        return 1
    return 0
def searchTopRight(i,j, input):
    if i-3 >=0 and j+3 < len(input[0]) and  input[i-1][j+1] == "M" and input[i-2][j+2] == "A" and input[i-3][j+3] == "S":
        return 1
    return 0
def searchRight(i,j, input):
    if j+3 < len(input[0]) and input[i][j+1] == "M" and input[i][j+2] == "A" and input[i][j+3] == "S":
        return 1
    return 0
def searchBottomRight(i,j, input):
    if i+3 < len(input) and j+3 < len(input[0]) and input[i+1][j+1] == "M" and input[i+2][j+2] == "A" and input[i+3][j+3] == "S":
        return 1
    return 0
def searchBottom(i,j, input):
    if i+3 < len(input) and input[i+1][j] == "M" and input[i+2][j] == "A" and input[i+3][j] == "S":
        return 1
    return 0
def searchBottomLeft(i,j, input):
    if i+3 < len(input) and j-3 >= 0 and input[i+1][j-1] == "M" and input[i+2][j-2] == "A" and input[i+3][j-3] == "S":
        return 1
    return 0
def searchLeft(i,j, input):
    if j-3 >= 0 and input[i][j-1] == "M" and input[i][j-2] == "A" and input[i][j-3] == "S":
        return 1
    return 0
def searchTopLeft(i,j, input):
    if i-3 >=0 and j-3 >=0 and input[i-1][j-1] == "M" and input[i-2][j-2] == "A" and input[i-3][j-3] == "S":
        return 1
    return 0

def xmasSearch2(input):
    sum = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == "A":
                sum+= searchAround(i,j, input)
    return sum

def searchAround(i,j,input):
    if i-1>=0 and j-1>=0 and i+1 <len(input) and j+1<len(input[0]):
        if checkTopMs(i,j,input) or checkRightMs(i,j,input) or checkLeftMs(i,j,input) or checkBottomMs(i,j,input):
            return 1
    return 0


def checkTopMs(i,j,input):
    if input[i-1][j-1] == "M" and input[i+1][j-1] == "M" and input[i+1][j+1] == "S" and input[i-1][j+1] == "S":
        return True
    return False
def checkRightMs(i,j,input):
    if input[i-1][j-1] == "S" and input[i+1][j-1] == "M" and input[i+1][j+1] == "M" and input[i-1][j+1] == "S":
        return True
    return False
def checkLeftMs(i,j,input):
    if input[i-1][j-1] == "M" and input[i+1][j-1] == "S" and input[i+1][j+1] == "S" and input[i-1][j+1] == "M":
        return True
    return False
def checkBottomMs(i,j,input):
    if input[i-1][j-1] == "S" and input[i+1][j-1] == "S" and input[i+1][j+1] == "M" and input[i-1][j+1] == "M":
        return True
    return False




def main():
    try:
        with open('input.txt', 'r') as file:
            input = []
            for line in file:
                input.append(list(line.strip()))
            
        
    except Exception as e:
        print(f"exception: {e}")
    print(f"xmasSearch : {xmasSearch(input)}")
    print(f"x-mas search: {xmasSearch2(input)}")
    
if __name__ == "__main__":
    main()