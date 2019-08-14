# Enter your code here. Read input from STDIN. Print output to STDOUT

if '__main__' == __name__:

    # define some functions
    mean = lambda x: sum(x) / len(x)
    cov = lambda x, y: mean([a*b for a,b in zip(x,y)]) - mean(x) * mean(y)

    N = int(input())
    nums = [int(i) for i in input().split()]
    nums = sorted(nums)

    # mean
    avg = mean(nums)
    print (round(avg, 1))

    # median 0, 1, 2, 3, 4, (5) 
    # 2+2/2 or 2+3/2 -> n//2+(n-1)//2 /2
    median = (nums[N//2] + nums[(N-2)//2]) / 2
    print (round(median, 1))

    # mode
    from collections import Counter
    counter = Counter(nums)
    mode = counter.most_common(1)[0][0]
    print (mode)

    # sdt = sqrt(var) = sqrt(cov(x,x))
    std = (cov(nums, nums))**0.5
    print (round(std, 1))

    # conf interval = mean ± 1.96 std / sqrt(N)
    print (round(avg - 1.96 * std/N**.5, 1),
        round(avg + 1.96 * std/N**.5, 1))


