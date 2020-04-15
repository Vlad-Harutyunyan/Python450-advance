tempList = [1,1,1]
removeElement = 1
removeType = int(input('please select removing type 1- remove method , 2- list comprehension : '))

if removeType == 1 :
    for elem in range(tempList.count(removeElement)) :
        tempList.remove(removeElement)
    print('Output ` ' ,tempList)
elif removeType == 2 :
    result = [x for x in tempList if x != removeElement ]
    print('Output ` ' , result)
else:
    print('wrong inputs')

#FIXED

