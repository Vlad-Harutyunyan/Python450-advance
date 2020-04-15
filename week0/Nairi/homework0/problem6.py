def problem6(a, b):
    if b > a:
        return problem6(b, a)
    if a % b == 0:
        return b
    return problem6(b, a % b)  
 
if __name__ == '__main__':
    #solution without recursion
    inpRange = [30,20]
    print(problem6(inpRange[0],inpRange[1]))

#FIXED