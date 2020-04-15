#practical 8
def practical8(arr):
    try :
        return sorted(set(arr))[-2]
    except :
        return 0.5
    
if __name__ == "__main__":
    #tests
    print(practical8([5, 5, 5]))
    print(practical8([5, 5, 5,5,5,5]))
    print(practical8([7 ,5, 5, 5,5,5,5,5,6]))
    print(practical8([3, 2, 5]))
    print(practical8([5, 1, 9]))
    print(practical8([-1, 5, 5]))



#Done