def calculateChecksum(input):
    intInput = [int(c) for c in input]
    outputArr = compactFilesystem(intInput)
    checkSum = 0
    print(outputArr)
    for i in range(len(outputArr)):
        checkSum += outputArr[i]*i
    return checkSum


def compactFilesystem(input):
    compact = []
    free = False
    right = len(input)-1
    id = 0
    
    for i in range(len(input)):
        if i > right:
            break
        if not free:
            temp = input[i]
            while temp > 0:
                compact.append(id)
                temp -= 1
            free = True
            id += 1
            continue
        elif free and input[i]>0:
            temp = input[i]
            while temp > 0:
                valRight = input[right]
                if valRight>0:
                    rightId = right//2
                    compact.append(rightId)
                    temp -= 1
                    input[right] -= 1
                else:
                    right -= 2
            free = False
        elif free and input[i==0]:
            free=False
    return compact

def main():
    input = ""
    with open('input.txt', 'r') as file:
        input = file.read()

    print(f"calculateChecksum : {calculateChecksum(input)}")
    # print(calculateChecksum([0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]))
if __name__ == "__main__":
    main()