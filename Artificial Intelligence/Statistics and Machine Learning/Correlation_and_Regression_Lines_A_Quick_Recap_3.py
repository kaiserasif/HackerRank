# https://www.hackerrank.com/challenges/correlation-and-regression-lines-8/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT


# phy = [float(i) for i in input().split()]
# his = [float(i) for i in input().split()]
phy = [15,12,8,8,7,7,7,6,5,3] 
his = [10,25,17,11,13,17,20,13,9,15]

# y = mx + b, m = cov(x,y) / var(x), b = mean(y) - mean(x).m
def mean(nums):
    return sum(nums) / len(nums)

def cov(nums1, nums2):
    return mean([x*y for x,y in zip(nums1, nums2)]) - mean(nums1)*mean(nums2)

m = cov(phy, his) / cov(phy, phy)
b = mean(his) - m * mean(phy)

print (round(m*10 + b, 1))

