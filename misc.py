
def cumsum(alist):
    res = list()
    for idx, val in enumerate(alist):
        if idx is 0:
            res.append(val)
        else:
            res.append(res[idx - 1] + val)
    return res


# compute mean
def slidingmean(alist, radius=1):
    asum = cumsum(alist)
    res = list()
    leftidx = rightidx = 0
    for idx, val in enumerate(asum):
        if idx - radius - 1 < 0:
            valleft = 0
        else:
            valleft = asum[idx - radius - 1]
        if idx + radius >= len(alist):
            rightidx = len(alist) - 1
        else:
            rightidx = idx + radius

        res.append(asum[rightidx] - valleft)
    return res


if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5]

    print(alist)
    print(slidingmean(alist,5))
