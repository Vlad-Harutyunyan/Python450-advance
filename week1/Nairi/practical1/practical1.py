#problem 1
def implication3(a,b,c):
    pass
#problem 2
def expr_value(stri):
    return "{:.2f}".format(eval(stri))

#problem 3
def recursive_or(arr):
    pass

#problem 4
def is_polyndrome(stri):
    pass

#problem 5 
def last_digit(num):
    res = 0
    for x in range(1,num+1):
        res += x * x
    return str(res)[-1]


#2 nel true 1 ini depqum 
if __name__ == "__main__":
    print('---- test 1 -----')
    print(expr_value('2+2*2'))
    print(expr_value('6-5*4/3+3-2*4'))

    print('---- test 5-----')
    print(last_digit(1000000))
    print(last_digit(950))


