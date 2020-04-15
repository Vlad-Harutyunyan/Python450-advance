def factCalc(num):
    fact = 1
    temp = 1
    while fact <= num :
        fact *= temp
        temp += 1
    return fact

if __name__ == "__main__":
    #tests
    print(factCalc(1))
    print(factCalc(2))
    print(factCalc(12))
    print(factCalc(24))
