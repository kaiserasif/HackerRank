# Enter your code here. Read input from STDIN. Print output to STDOUT

if "__main__" == __name__:
    N = int(input())
    mth, phy, chm = [], [], []

    for _ in range(N):
        m, p, c = [int(i) for i in input().split()]
        mth.append(m)
        phy.append(p)
        chm.append(c)

    # define functinos
    mean = lambda x: sum(x) / len(x)
    cov = lambda x, y: mean([a*b for a,b in zip(x,y)]) - mean(x) * mean(y)

    # corr = cov / (std1 * std2) = cov / sqrt(var1 * var2)
    m_std = cov(mth, mth)**.5
    p_std = cov(phy, phy)**.5
    c_std = cov(chm, chm)**.5

    print( round(cov(mth, phy) / m_std / p_std, 2) )
    print( round(cov(chm, phy) / c_std / p_std, 2) )
    print( round(cov(mth, chm) / m_std / c_std, 2) )