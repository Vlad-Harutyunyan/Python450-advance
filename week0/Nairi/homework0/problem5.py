def decimalToBinary(x):
    return int(bin(x)[2:])

if __name__ == '__main__':
    inpValue = int(input('please enter number : '))
    result = decimalToBinary(inpValue)
    result = sum([int(k) for k in str(result)])
    print(result)