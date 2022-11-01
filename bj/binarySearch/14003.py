import bisect as bs

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
cp = [-float('inf')]

for i in range(1, n+1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp)-1
    else:
        dp[i] = bs.bisect_left(cp, nums[i])
        cp[dp[i]] = nums[i]
print(len(cp)-1)

max_idx, ans = max(dp)+1, []
for i in range(n, 0, -1):
    if dp[i] == max_idx-1:
        ans.append(nums[i])
        max_idx = dp[i]
print(*ans[::-1])
