#symbol no more 1 , number not a sring only number
def foo():
    inpnum = (input('enter length,please : '))
    while not inpnum.isdecimal():
        print('error : wrong input ,please neter number ')
        inpnum = (input('enter length,please : '))
    inpnum = int(inpnum)
    while True :
        inpsymbol = input('enter symbol for fill, please :')
        if len(inpsymbol) > 1 :
            print('please insert one symbol for length')
        else :
            inptext = input('enter text , please  : ')
            ln = inpnum  - len(inptext)
            if ln > 1 :
                result = ln * inpsymbol
                return '{}{}'.format(result,inptext)
            else :
                return inptext
if __name__ == '__main__':
   print( foo() )