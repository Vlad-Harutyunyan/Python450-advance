#practiacl 4
def factorialLoop(num):
    summ = 1
    for x in range(1,num+1):
        summ = summ * x
    return summ

#Some fixes
def factorialRec(num):
    return 1 if num == 1 or num == 0 else num * factorialRec(num - 1);
print(factorialRec(4))
print(factorialLoop(4))

#Done