def sumOfMultiplies(input):
    i = 0
    sum = 0
    do = True
    while i < len(input):
        if do:
            if i+6< len(input) and input[i] == "d" and input[i+1] == "o" and input[i+2] == "n" and input[i+3]== "'" and input[i+4] == "t" and input[i+5] == "(" and input[i+6] == ")":
                do = False
            if do and i+3< len(input) and input[i] == "m" and input[i+1] == "u" and input[i+2] == "l" and input[i+3]== "(":
                i+=4
                num1 = ""
                while i<len(input) and isDigit(input[i]):
                    num1 = f"{num1}{input[i]}"
                    i+=1
                if i < len(input) and isDigit(input[i-1]) and input[i] == ",":
                    i+=1
                    num2 = ""
                    while i <len(input) and isDigit(input[i]):
                        num2 = f"{num2}{input[i]}"
                        i+=1
                    if i < len(input) and input[i] == ")":
                        sum+= int(num1) * int(num2)

        else:
            if i+3< len(input) and input[i] == "d" and input[i+1] == "o" and input[i+2] == "(" and input[i+3]== ")":
                do=True

        i+=1
        
    return sum

def isDigit(c):
    if c in "0123456789":
        return True
    return False

def main():
    try:
        with open('input.txt', 'r') as file:
            input = file.read()
    except Exception as e :
        print(f"exception : {e}")
    print(f"sumOfMultiples : {sumOfMultiplies(input)}")
    

if __name__ == "__main__":
    main()