
tempList = [[[1,2,3,1],[1,2,3,1]],[1,2,3],[[1,2,3,1],[1,2,3,1]]] #checked ,passed

removeType = int(input('please select removing type 1- remove method , 2- list comprehension , 3 -remove way with minimum symbols: '))
result = []

def type3(lst):
    print([i for n, i in enumerate(tempList) if i not in tempList[:n]] )

if removeType == 1  :
    for elem in tempList :
        if not elem in result:
            result.append(elem)
    print('Output ` ',result)

if  removeType == 2 :
    result = [ tempList[x] for x in range(len(tempList)) if tempList[x] not in tempList[x+1:] ]
    print('Output ` ', result)

if removeType == 3 :
    type3(tempList)

#FIXED #type 3 working wrong when we have list in list ov elements need to be fixed
