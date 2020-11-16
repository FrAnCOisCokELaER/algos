#time complexity : O(N) (insertin in a dll is O(1))
import collections


def cumsum(alist):
    res = list()
    for idx in range(len(alist)):
        if idx is 0:
            res.append(alist[idx])
        else:
            res.append(res[idx - 1] + alist[idx])
    return res


# compute mean
def slidingmean(alist, radius=1):
    asum = cumsum(alist)  # O(N)
    res = list()
    for idx, val in enumerate(asum):
        if idx - radius - 1 < 0:
            valleft = 0
        else:
            valleft = asum[idx - radius - 1]
        if idx + radius >= len(alist):
            valright= asum[len(alist) - 1]
        else:
            valright = asum[idx + radius]
        res.append(valright - valleft)
    return res

#flood fill
#geiven an 2D matrix replace the targetcolor by repcolor
# def floodfill(im, startposition, repcolor ):
#     #
#     targetcolor = im[startposition]
#     import collections
#     pixelq = collections.deque()
#     pixelq.append(startposition)
#     while len(pixelq) > 0:
#         currpix = pixelq.pop()
#         im[currpix] = repcolor
#         pixelq.append(currpix + 1)
#     # 4 neighbor adjacency graph



if __name__ == "__main__":
    alist = [1, 2, 3, 4, 5]
    print(alist)
    print(slidingmean(alist,2))
