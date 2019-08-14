# https://www.hackerrank.com/challenges/correlation-and-regression-lines-7/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT

Score1 = [15,12,8,8,7,7,7,6,5,3] 
Score2 = [10,25,17,11,13,17,20,13,9,15]
phy = Score1 # [float(i) for i in input().split()]
his = Score2 # [float(i) for i in input().split()]

def mean(nums):
    return 1.0 * sum(nums) / len(nums)

def cov(nums1, nums2):
    return mean([x*y for x,y in zip(nums1, nums2)]) - mean(nums1) * mean(nums2)

print ( round(cov(phy, his) / cov(phy, phy) , 3) ) 
