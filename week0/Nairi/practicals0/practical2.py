#practical 2

def type1(l):
    sets = [set(x) for x in l]
    return len(sets[0].intersection(*sets[1:]))

def type2(l):
    first = [char for char in l[0]]
    cnt = len(l) - 1
    result = 0

    for elem in range(len(first)):
        temp = 0
        for x in range(1,len(l)):
            if first[elem] in l[x]: 
                temp += 1
        if temp == cnt :
            result += 1

    return result

if __name__ == "__main__" :
    print('------- test 1 ------- ')
    l  = ['aac','aacb','aac','aace']
    print(type1(l))
    print(type2(l))
    print('------- test 2 ------- ')
    l  = ['aac','aab','aae']
    print(type1(l))
    print(type2(l))
    print('------- test 3 ------- ')
    l  = ['a','b','c']
    print(type1(l))
    print(type2(l))
    

