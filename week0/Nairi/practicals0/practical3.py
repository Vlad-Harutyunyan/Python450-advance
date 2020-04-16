#practical 3
def practical3(arr):
    nums = []
    for x in arr:
        num = []
        while x > 0 :
            num.append( x%10 )
            x //= 10
        nums.append(num)
    for elem in range(len(nums)):
        cnt = 0
        for digit in nums[elem] :
            if nums[elem].count(digit) > 1 :
                cnt += 1
        if cnt < 1 :
            return arr[elem]
    else :
        return -1

print(practical3([101, 110, 220, 100, 103, 606, 603]))

#Done