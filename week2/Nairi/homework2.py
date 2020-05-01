#imports
from collections import defaultdict

#problem1
def bisect_position(arr:list,n:int) -> int :
    for x in arr:
        if n >= x :
            pass
        else:
            return arr.index(x)
    return len(arr)
      
#problem2

def all_sums(numm:int) -> list :
    cnt = numm//2
    left = list(range(1,cnt+1))
    right = list(range(cnt,numm))
    r = []
    
    for x in left :
        for y in right :
            if x + y == numm :
                r.append((x,y))
    return r   

#problem3

def duplicate_characters(stri:str) -> dict :
    d = defaultdict(int)
    res = set()
    for x in stri:
        d[x] += 1
        if d[x] > 1 and x != ' ':
            res.add(x)
   
    return res

#problem4        

def compare_lists(arr1:list,arr2:list) -> bool :
    if len(arr1) != len(arr2) :
        return False
    else :
        for elem in range(len(arr1)):
            if arr1[elem] in arr2  :
                arr2[arr2.index(arr1[elem])] = None
            else :
                return False
    return True

#problem5
#heappush implementations
def heappush(heap, val):
    le = len(heap)
    heap.append(val)
    while le > 0:
        parent = (le - 1) // 2
        if heap[parent] <= heap[le]: 
            break
        heap[le], heap[parent] = heap[parent], heap[le]
        le = parent
        pass
    pass


def heapq(arr:list,n:int) -> list:
    h = []
    arr.append(n)
    for value in arr :
        heappush(h,value)
    return h



#problem6

def sort_list(arr:list,order='ascending') -> list:
    result = []
    if len(arr) == 1 :
        return arr

    mid = len(arr) // 2
    left = sort_list(arr[:mid])
    right = sort_list(arr[mid:])
    x , y = 0 , 0

    while x < len(left) and y < len(right) :
        if left[x] > right[y]:
            result.append(right[y])
            y += 1
        else :
            result.append(left[x])
            x += 1

    result += left[x:]
    result += right[y:]

    if order == 'ascending' :
        return result
    elif order == 'descending' :
        return result[::-1]



if __name__ == "__main__" :
    print('1) ------ bisect position ------')
    print(bisect_position([1,2,3,6], 4))
    print(bisect_position([1,2,3,6], 3))
    print(bisect_position([1,2,2,2], 2))
    print(bisect_position([1,2,3,5,7], 8))

    print('2)------ all sums -------')
    print(all_sums(7))
    print(all_sums(4))
    print(all_sums(2))
    print(all_sums(77))
    print(all_sums(10))

    print('3)--------- defaultdict (duplications)   ')
    print(duplicate_characters('hellllllo world'))
    print(duplicate_characters('Here we have some duplicates'))
    print(duplicate_characters('no duplicates'))

    print('4)---- compare list -----')
    print(compare_lists([1,2,3],[3,2,1,1]))
    print(compare_lists([1,2,4,3],[3,2,1,4]))
    print(compare_lists([1,2,1,3],[3,2,1,4]))
    print(compare_lists([1,1,1,4],[3,2,1,4]))
    print(compare_lists([1,2,3,4],[1,2,3,4]))
    print(compare_lists([-1,-2,3,4],[3,4,-1,-2]))
    print(compare_lists([-1,-2,3,4,-1,-2,1],[-1,-2,3,4,-1,-2,1]))
    print(compare_lists([1,2,1,2,1,2],[1,2,1,2,1,2]))
    print(compare_lists([1,2,1,1,1,2],[1,2,1,2,1,2]))

    print('5)----------- heapq ----------------')
    print(heapq([1,3,5,7,9],2))
    print(heapq([1,2,3,4],5))

    print('6) -------- sorting list with order ------- ')
    print(sort_list([1,4,3,2], 'descending'))
    print(sort_list([4,3,2,1]))
    print(sort_list([6,2,4,6], 'descending'))
    print(sort_list([3,3,2,1]))
    print(sort_list([4,1,1,1], 'descending'))

#         1
#     3       5
# 7       9