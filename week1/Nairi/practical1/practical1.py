#problem 1
def implication3(a:int,b:int,c:int) -> bool:
    return a and b and not c

#problem 2
def expr_value(s:list) -> float:
    if '+' in s :
        return expr_value(s[:s.index('+')])+expr_value(s[s.index('+')+1:])
    if '-' in s :
        return expr_value(s[:s.index('-')])-expr_value(s[s.index('-')+1:])
    if '*' in s and '/' in s :
        if s.index('*') < s.index('/'):
            return expr_value(s[:s.index('*')]) * expr_value(s[s.index('*')+1:])
    if '/' in s :
        return expr_value(s[:s.index('/')]) / expr_value(s[s.index('/')+1:])
    if '*' in s :
        return expr_value(s[:s.index('*')]) * expr_value(s[s.index('*')+1:])
    
    return float(s)
    # return "{:.2f}".format(eval(s))

#problem 3 
def recursive_or(arr:list) -> bool :
    return arr[0] or (len(arr) > 1 and recursive_or(arr[1:]))

#problem 3-1
def quick_or(arr:list) -> bool :
    return True in arr
    # return bool(sum(arr))

#problem 4
def is_polyndrome(stri:str) -> bool :
    pass


#problem 5 
def last_digit(num):
    res = 0
    for x in range(1,num+1):
        res += x * x
    return int(str(res)[-1])


#2 nel true 1 ini depqum 
if __name__ == "__main__":
    print('---- implication 3 -----')
    print(implication3(1,0,1))
    print(implication3(1,0,0))
    print(implication3(1,1,0))
    print(implication3(0,0,0))

    print('---- Math exression in string -----')
    print(expr_value('2+2*2'))
    print(expr_value('6-5*4/3+3-2*4'))
    print('---- Recursive or -----')
    print(recursive_or([False,False,True]))
    print(recursive_or([False,False,False]))
    print('---- Quick or -----')
    print(quick_or([False,False,True]))
    print(quick_or([False,False,False]))
    print('---- Convert Polindrome -----')
    print(is_polyndrome('vlad'))

    print('---- Last digit -----')
    print(last_digit(1000000))
    print(last_digit(950))



