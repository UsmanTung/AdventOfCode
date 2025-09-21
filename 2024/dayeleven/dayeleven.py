def afterXBlinks(blinks, input):
    result = input
    for i in range(blinks):
        j = 0
        while j < len(result):
            if result[j] == "0":
                result[j] = "1"
                j += 1
            elif len(result[j]) % 2 == 0:
                middle = len(result[j]) // 2
                left = result[j][0:middle]
                right = result[j][middle:len(result[j])]
                if int(right) == 0:
                    right = "0"
                else:
                    while right[0] == "0":
                        right = right[1:len(right)]
                del result[j]
                result.insert(j, right)
                result.insert(j, left)
                j += 2

            else:
                result[j] = str(int(result[j]) * 2024)
                j += 1
    return len(result)

def main():
    with open('input.txt', 'r') as file:
        input = file.read().split()
    print(f"after 25 Blinks :{afterXBlinks(25, input)}")
if __name__ == "__main__":
    main()