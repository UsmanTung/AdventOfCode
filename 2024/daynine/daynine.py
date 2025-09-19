def calculateChecksum(input):
    intInput = [int(c) for c in input]
    outputArr = compactFilesystem(intInput)
    checkSum = 0
    for i in range(len(outputArr)):
        checkSum += outputArr[i]*i
    return checkSum

def calculateChecksum2(input):
    outputArr = compactFilesystem2(input)
    checkSum = 0
    index = 0
    for i in range(len(outputArr)):
        id, length = outputArr[i]
        if id != ".":
            for i in range(int(length)):
                checkSum += int(id)*(index)
                index += 1
        else:
            index += int(length)
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

def compactFilesystem2(input):
    linkedArr = link(input)
    seen = set()
    i = len(linkedArr)-1
    while i >= 0:
        id, length = linkedArr[i]
        if id not in seen:
            for j in range(1, i):
                if linkedArr[i][0] == ".":
                    break
                if linkedArr[j][0] == "." and int(linkedArr[j][1]) >= int(length):
                    linkedArr.insert(j,(id, length))
                    if int(linkedArr[j+1][1]) - int(length) > 0:
                        linkedArr[j+1] = (".", str(int(linkedArr[j+1][1]) - int(length)))
                        linkedArr[i+1] = (".", length)
                    else:
                        del linkedArr[j+1]
                        linkedArr[i] = (".", length)
                    break
            seen.add(id)
        i-=1
    return linkedArr

def link(input):
    result = []
    id = 0
    for i in range(len(input)):
        if i % 2 == 0:
            result.append((str(id), input[i]))
            id += 1
        else:
            if input[i] != "0":
                result.append((".",input[i]))
    
    return result

def main():
    input = ""
    with open('input.txt', 'r') as file:
        input = file.read()

    print(f"calculateChecksum : {calculateChecksum(input)}")
    print(f"calculateChecksum of compact2 : {calculateChecksum2(input)}")
    # print(calculateChecksum([0,0,9,9,8,1,1,1,8,8,8,2,7,7,7,3,3,3,6,4,4,6,5,5,5,5,6,6]))
if __name__ == "__main__":
    main()