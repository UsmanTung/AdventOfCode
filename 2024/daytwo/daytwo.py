def countSafe(input):
    count = 0
    for array in input:
        for i in range(len(array)):
            arr = [e for ind, e in enumerate(array) if ind!=i]
            safe = True
            increasing = True
            for i in range(1, len(arr)):
                if i == 1:
                    if arr[i-1] > arr[i]:
                        increasing = False
                else:
                    if increasing and arr[i-1] > arr[i]:
                        safe=False
                        break
                    elif not increasing and arr[i-1] < arr[i]:
                        safe=False
                        break
                if 1 > abs(arr[i-1] - arr[i]) or 3 < abs(arr[i-1] - arr[i]):
                    safe=False
                    break
                
            if safe:
                count+=1
                break
        
    return count

def main():
    input = []
    try:
        with open('input.txt', 'r') as file:
            for line in file:
                arr = line.split()
                temp = []
                for v in arr:
                    temp.append(int(v))
                input.append(temp)
                
    except Exception as e:
        print(f"Exception {e}")
    
    print(f"Part one: {countSafe(input)}")

if __name__ == "__main__":
    main()