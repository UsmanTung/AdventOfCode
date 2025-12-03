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
    ids = sorted({id for id, _ in linkedArr if id != "."},
                 key=lambda x: int(x), reverse=True)
    for fid in ids:
        fi = next(i for i, (idv, _) in enumerate(linkedArr) if idv == fid)
        length = linkedArr[fi][1]
        target = None
        for j in range(0, fi):
            if linkedArr[j][0] == "." and int(linkedArr[j][1]) >= int(length):
                target = j
                break
        if target is None:
                continue
        free_len = linkedArr[target][1]
        linkedArr.insert(target, (fid, length))
        rem = free_len - length
        if rem > 0:
            linkedArr[target + 1] = (".", rem)
        else:
            del linkedArr[target + 1]
        fi_old = next(k for k in range(target + 1, len(linkedArr))
                      if linkedArr[k][0] == fid)

        linkedArr[fi_old] = (".", length)

    return linkedArr

def link(input):
    result = []
    id = 0
    for i in range(len(input)):

        if i % 2 == 0:
            result.append((str(id), int(input[i])))
            id += 1
        else:
            if input[i] != "0":
                result.append((".", int(input[i])))
    
    return result

def main():
    input = ""
    with open('input.txt', 'r') as file:
        input = file.read()

    print(f"calculateChecksum : {calculateChecksum(input)}")
    print(f"calculateChecksum of compact2 : {calculateChecksum2(input)}")
    print(f"calculateChecksum of example compact2 : {calculateChecksum2("2333133121414131402")}")
    #print(f"link : {link(input)}")
if __name__ == "__main__":
    main()