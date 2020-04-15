#practical 2

def type1(l):
    sets = [set(x) for x in l]
    print(len(sets[0].intersection(*sets[1:])))

def type2(l):
    pass




if __name__ == "__main__" :
    l  = ['aaae','aaaeb','aaaecfc']
    type1(l)
    type2(l)
    

