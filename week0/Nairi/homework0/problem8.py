def getMissingNumber(arr): 
    n = len(arr) 
    total = (n + 1)*(n + 2)/2
    arrSum = sum(arr) 
    return total - arrSum 

if __name__ == '__main__':
    inpList = [1,2,3] 
    miss = getMissingNumber(inpList) 
    print(miss) 