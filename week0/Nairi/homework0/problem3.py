word = input('please enter word for cheking : ')
chekingType = int(input('please select cheking type 1 - with for loop ,  2 - in one line  '))


def type1(word):
    for i in range(0, len(word)//2):  
        if word[i] != word[len(word)-i-1]: 
           return False
    return True


if chekingType == 1 :
    print( type1(word) )

elif chekingType == 2 :
    print( word == word[::-1] )

else:
    print('wrong inputs')

#FIXED