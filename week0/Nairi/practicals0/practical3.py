#practical 3
def practical3(arr):
    nums = []
    for x in arr:
        num = []
        while x > 0 :
            num.append( x%10 )
            x //= 10
        nums.append(num)
    results = []
    for elem in nums:
        cnt = 0
        for digit in elem :
            if elem.count(digit) > 1 :
                cnt += 1
        if cnt < 1 :
            results.append(elem)
    if len(results) > 0 :
        return results
    else :
        return -1

print(practical3([101, 110, 220, 100, 103, 606, 603]))

#Done