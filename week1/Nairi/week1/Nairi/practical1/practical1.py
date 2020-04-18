#problem 1
def implication3(a,b,c):
    pass
#problem 2
def expr_value(stri):
    return "{:.2f}".format(eval(stri))

#problem 3
def recursive_or(arr,i=0):
    return recursive_or(arr,i+1) if arr[i] is False and len(arr) < i else False if arr[i] is True  True else False

#problem 4
def is_polyndrome(stri):
    pass

#problem 5 
def last_digit(num):
    res = 0
    for x in range(1,num+1):
        res += x * x
    return int(str(res)[-1])


#2 nel true 1 ini depqum 
if __name__ == "__main__":
    print('---- Math exression in string -----')
    print(expr_value('2+2*2'))
    print(expr_value('6-5*4/3+3-2*4'))
    print('---- Recursive or -----')
    print(recursive_or([False,False,True]))
    print(recursive_or([False,False,False]))

    print('---- Convert Polindrome -----')
    print(is_polyndrome('vlad'))

    print('---- Last digit -----')
    print(last_digit(1000000))
    print(last_digit(950))



