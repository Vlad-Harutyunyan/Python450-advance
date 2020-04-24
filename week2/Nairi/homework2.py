#problem1

def bisect_position(arr:list) -> int :
    pass
#problem2

def all_sums(numm:int) -> tuple :
    pass

#problem3

def duplicate_characters(stri:str) -> dict :
    pass

#problem4

def compare_list(arr1:list,arr2:list) -> bool :
    if len(arr1) != len(arr2) :
        return False
    else :
        inds = []
        for elem in range(len(arr1)):
            if arr1[elem] in arr2 and arr2.index(arr1[elem]) not in inds :
                inds.append(arr2.index(arr1[elem]))
                arr2[arr2.index(arr1[elem])] = None
        return len(inds) == len(arr1) and len(inds) == len(arr2)

#problem5

def heapq(arr:list,n:int) -> list :
    pass

#problem6

def sort_list(arr:list,order='ascending') -> list:
    pass 

if __name__ == "__main__" :
    print('---- compare list -----')
    print(compare_list([1,2,3],[3,2,1,1]))
    print(compare_list([1,2,4,3],[3,2,1,4]))
    print(compare_list([1,2,1,3],[3,2,1,4]))
    print(compare_list([1,1,1,4],[3,2,1,4]))
    print(compare_list([1,2,3,4],[1,2,3,4]))
    print(compare_list([-1,-2,3,4],[3,4,-1,-2]))
    print(compare_list([-1,-2,3,4,-1,-2,1],[-1,-2,3,4,-1,-2,1]))
    print(compare_list([1,2,1,2,1,2],[1,2,1,2,1,2]))
    print(compare_list([1,2,1,1,1,2],[1,2,1,2,1,2]))





