def sumOfDifferences(arr1, arr2):
    arr1.sort()
    arr2.sort()
    sum = 0
    for i in range(len(arr1)):
        sum+= abs(arr1[i] - arr2[i])
    return sum




def main():
    arr1 = []
    arr2 = []
    try:
        with open('input.txt', 'r') as file:
            for line in file:
                a, b = line.split("   ")
                arr1.append(int(a))
                arr2.append(int(b))
    except Exception as e:
        print(f"An error occurred: {e}")
    print(sumOfDifferences(arr1, arr2))


if __name__ == "__main__":
    main()
