# doesn't work
def maxSubArray1(nums):
        n = 0
        m = len(nums)
        sum = 0
        min = 0
        for i in range(m):
            sum += nums[i]
            if sum < min:
                min = sum
                n = i + 1
        sum = 0
        min = 0
        for j in range(m-1, -1, -1):
            sum += nums[j]
            if sum < min:
                min = sum
                m = j
        ans = 0
        for k in nums[n:m]:
            ans += k
            print(ans)
        return(ans)
# doesn't work   
def maxSubArray2(nums):
    n = 0
    m = len(nums)
    sum = 0
    min = 0
    for i in range(m-1):
        sum += nums[i]
        if sum < min:
            min = sum
            n = i + 1
    sum = 0
    min = 0
    for j in range(len(nums)-1, 0, -1):
        sum += nums[j]
        print("sum", sum)
        if sum < min:
            min = sum
            print("min", min)
            m = j
    print(n, m)
    ans = 0
    if m <= n or n == len(nums)-1 or m == 1:
        ans = nums[0]
        for i in nums:
            if i > ans:
                ans = i
        return(ans)
    else:
        for k in nums[n:m]:
            ans += k
        return(ans)
# works
def maxSubArray(nums):
    windowSum = nums[0]
        maxSum = nums[0]
        
        for i in range(1,len(nums)):
            windowSum = max(windowSum+nums[i], nums[i])
            maxSum = max(windowSum, maxSum)
        return maxSum