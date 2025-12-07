from collections import Counter

def sumOfInvalid(data):
    total = 0
    i = 0
    while i+1 < len(data):
        for j in range(int(data[i]), int(data[i+1])+1):
            strj = str(j)
            lenj = len(strj)
            index2 = lenj//2
            invalid = True
            if lenj % 2 != 0:
                continue
            for v in range(lenj//2):
                if strj[v] != strj[index2]:
                    invalid = False
                    break
                index2 += 1
            if invalid:
                total += j
            
        i += 2
    return total

def sumOfInvalid2(data):
    total = 0
    i = 0
    while i+1 < len(data):
        for j in range(int(data[i]), int(data[i+1])+1):
            strj = str(j)
            for y in range(1, len(strj)//2 + 1):
                if len(strj) % y != 0:
                    continue
                valid=True
                window = y
                while window + y <= len(strj):
                    if strj[window - y:window] != strj[window:window + y]:
                        valid=False
                        break
                    window += y
                if valid:
                    total += j
                    break
        i += 2
    return total


def main():
    with open("2025/day2/input.txt") as f:
        data = f.read().strip()
        data = data.replace("-", ",")
        ranges = data.split(",")
    print(sumOfInvalid2(ranges))


if __name__=="__main__":
    main()