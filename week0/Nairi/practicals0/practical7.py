#practical7
def practical7(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    str1 = ' '.join(map(str, arr1))
    str2 = ' '.join(map(str, arr2))
    if len(str1) != len(str2):
        return False

    return str1 in str2 + ' ' + str2


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