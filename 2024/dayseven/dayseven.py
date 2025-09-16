def sumOfValidEquations(answers, values):
    totalSum = 0
    for i in range(len(answers)):
        equalToAns = recurse(answers[i], values[i], 1, values[i][0])
        if equalToAns:
            totalSum+=answers[i]
    return totalSum
            
def recurse(answer, values, i, total):
    if i >= len(values) and total!=answer:
        return False
    if total == answer and len(values) <= i:
        return True
    return recurse(answer, values, i+1, total+values[i]) or recurse(answer, values, i+1, total*values[i])
    

def main():
    with open('input.txt', 'r') as file:
        answers = []
        values = []
        for line in file:
            answer, preValues = line.split(":")
            answers.append(int(answer))
            values.append([int(ele) for ele in preValues.strip().split()])

    print(f"sum of valid equations: {sumOfValidEquations(answers, values)}")

if __name__ == "__main__":
    main()