#problem 1
def all_positive(*args):
    return any(x < 0 for x in args ) 

#problem 2
def xor3(a,b,c):
    pass
#problem 3
def mirror_string(txt):
    #alphabet with lower and upper cases 
    alphabetLower = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    res = ''
    #slice words for white spaces
    tmp = txt.split(' ')

    for t in tmp :
        r = ''
        mirr = str.maketrans(alphabetLower, alphabetLower[::-1], ' ')

        r = t.translate(mirr)
        r = r.swapcase()
        res += r + ' '

    return res

#problem 4
def bit_concat (arr):
    pass


#problem 5


#problem 6
def only_names(x):
    if len(x) != 0 :
        return x

#problem 7
discriminant = lambda a,b,c: b**2 - 4 * (a*c)

#problem 8
# full_name = lambda arr1,arr2 : arr1[0][0] + ' ' + arr[1]


if __name__  == '__main__' :
    print('problem 1) -----------  All positive function tests -----------')
    print(all_positive(-1,2,3,4,1))
    print(all_positive(2,3,4,1))
    print(all_positive(7,2,6,-3,10))

    print('problem 2) -----------  Logical xor for 3 arguments -----------')


    print('problem 3) -----------  Mirror string  -----------')
    print(mirror_string('Hello, World!'))
    print(mirror_string('221B Baker Street'))
    print(mirror_string('Hello'))
    print(mirror_string('WorldD'))


    print('problem 6) -----------  Only names , filter empty strings from list  -----------')
    p6_1 = ['Vlad','Nairi','Zara','','']
    p6_2 = ['Name1','','','','Name2','']
    print(list(filter(only_names,p6_1)))
    print(list(filter(only_names,p6_2)))

    print('problem 7) ----------- Calculate discriminant  -----------')
    print(discriminant(1,2,1))
    print(discriminant(4,8,0))

    print('problem 8) ----------- Full Name  -----------')
    # p8_1 = ['Nairi','Vlad']
    # p8_2 = ['Hakobyan','Poghosyan']
    # print(list(map(full_name,p8_1,p8_2)))
