#practical7
def practical7(list1, list2): 
    # doubling list 
    tempList = list1 * 2
    for x in range(0, len(list1)): 
        cnt = 0 
          
        for j in range(x, x + len(list1)): 
            if list2[cnt]== tempList[j]: 
                cnt += 1
            else: 
                break
        if cnt == len(list1): 
            return True 

    return False


if __name__ == "__main__" :
    test1 = [[1, 2, 3], [2, 3, 1] ]
    test2 = [[1, 3, 4, 5, 2], [5, 2, 1, 3, 4] ]
    test3 = [[1, 2, 3], [3, 2, 1] ]
    test4 = [[1,3,4],[4,1,3,2]]
    print(practical7(test1[0],test1[1] ))
    print(practical7(test2[0],test2[1] ))
    print(practical7(test3[0],test3[1] ))
    print(practical7(test4[0],test4[1] ))


# Done