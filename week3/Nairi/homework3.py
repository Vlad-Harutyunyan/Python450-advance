import numpy as np

def arr_replace(arr:list) -> list:
    res = np.array(arr)
    res[res%2==1] = 0
    return res

def arr_replace_where(arr:list) -> list :
    res = np.array(arr)
    return np.where(res%2==0, 0 , res)


def arr_repeat(arr:list) -> list :
    res = np.array(arr)
    return np.repeat(a = res , repeats=3)


def arr_join(arr:list) -> list :
    res = np.array(arr)
    return np.tile(res,3)
    
def arr_intersection(arr1:list,arr2:list) -> list :
    return np.intersect1d(arr1,arr2)


def arr_random(shape1:tuple) -> list :
    return np.random.uniform(5,10,size=shape1)

if __name__ == "__main__" :
    print('1) Array Replace odd')
    print(arr_replace([1,2,3,4]))
    print('2) Array Replace even')
    print(arr_replace_where([1,2,3,4,5,6,2,8]))
    print('3) Array Repeat ')
    print(arr_repeat([1,2,3]))
    print(arr_repeat([1,1,2,2]))
    print('4) Array Join ')
    print(arr_join([1,2,3]))
    print(arr_join([1,1,2,2]))
    print('5) Intersaction')
    print(arr_intersection([1,1,2], [2,1,1]))
    print(arr_intersection([1,2,3], [3,2,1]))
    print('6) Array Random')
    print(arr_random((2,2)))
