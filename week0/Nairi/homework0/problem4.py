number = int(input('please enter number : '))
checkingType = int(input('please select cheking type 1 - with for loop ,  2 - with minimum symbols  '))

def t2(n):
    return sum([int(k) for k in str(n)])

if __name__ == "__main__":
    
    if checkingType == 1 :
        result = 0 
        while number > 0 :
            result += number % 10
            number //= 10
        print(result)
    elif checkingType == 2 :
        print(t2(number))

    else :
        print('wrong inputs')

#FIXED