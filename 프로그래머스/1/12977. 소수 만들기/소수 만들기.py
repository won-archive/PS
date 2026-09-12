import math

def solution(nums):
    def is_prime(n):
        if n % 2 == 0:
            return 0
    
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return 0
        return 1
    
    length = len(nums)
    ans = 0
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                temp = nums[i] + nums[j] + nums[k]
                ans += is_prime(temp)

    return ans