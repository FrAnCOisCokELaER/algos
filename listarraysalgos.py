# https://www.tutorialspoint.com/python/python_recursion.htm
# append is modifying the list in place, + create a new list from two lists
# complexity ois O(n log(n))
# logarithm time to divide and linear time to merge n elements
def msort(tosort):
    # divide
    halfindex = (int)(len(tosort) / 2)
    if halfindex == 0:
        return tosort
    else:
        # merge
        def merge(left, right):
            if not left:
                return right
            if not right:
                return left
            if left[0] <= right[0]:
                return [left[0]] + merge(left[1:], right)
            else:
                return [right[0]] + merge(left, right[1:])

        return (merge(msort(tosort[0:halfindex]), msort(tosort[halfindex:])))


# complexity ois O(n log(n))
# logarithm time to divide and linear time to compare n elements
# can be n^2 if pivot is taken as the max value of a sorted array
def qsort(tosort):
    halfindex = (int)(len(tosort) / 2)
    if halfindex == 0:
        return tosort
    else:
        #complexity is O(1)
        def mergelists(left, right, pivot):
            if not left:
                return [pivot] + right
            if not right:
                return left + [pivot]
            return left + [pivot] + right

        pivotval = tosort[halfindex]
        tosort.pop(halfindex)
        left = list(filter(lambda x: x <= pivotval, tosort))
        right = list(filter(lambda x: x > pivotval, tosort))

        return mergelists(qsort(left), qsort(right), pivotval)


# a unique algorithm in n^2 : (n)+(n-1)+(n-2) ... = O(n* (n+1) )/2 = O(n^2)
def unique(tosort):
    if not tosort:
        return list()
    return [tosort[0]] + unique(list(filter(lambda x: x != tosort[0], tosort)))


# using a set is reducing complexity to O(n) % hashmap collision
def uniquebest(tosort):
    if not tosort:
        return list()
    res = set()
    for elt in tosort:
        res.add(elt)
    return list(res)


# divide an conquer binary search on sorted list
def bsearch(tosearch, idx0, idxn, val):
    if idxn < idx0:
        return None
    else:
        halfindex = idx0 + ((idxn - idx0) // 2)  #idx0 is used for global indexing  as we always pass tosearch arrays
                                                 #and not the subarrays
        if tosearch[halfindex] > val:
            return bsearch(tosearch, idx0, halfindex - 1, val)
        elif tosearch[halfindex] < val:
            return bsearch(tosearch, halfindex + 1, idxn, val)
        else:
            return halfindex

#binary search in a rotated array already sorted by ascending order
#find the pivot and then do a regular binary search on the two subarrays
def bsearchrotated(tosearch, idx0, idxn, val):
    #find pivot
    pivot = None
    for idx in range(0, len(tosearch) - 1): # the pivot is the one element that have a right neightbour strictly lesser
        if tosearch[idx] > tosearch[idx+1]:
            pivot = idx
    if pivot:
        left = tosearch[0:pivot]
        right = tosearch[pivot+1:]
        if val >= left[0]:
            return bsearch(left, 0, len(left)-1, val)
        else:
            return (bsearch(right, 0, len(right)-1, val) + pivot) + 1
    else:
        return tosearch #no pivot found means the list is not rotated

#permform a random shuffle of array elements
from random import randint
def randomshuffle(alist):
    def shuffleindex(size):
        shuffl = []
        while len(shuffl) is not size:
            anint = randint(0, len(alist)-1) #not like range ! rand includes last range value
            already = False
            for elt in shuffl:
                if elt is anint:
                    already = True
                    break
            if not already:
                shuffl.append(anint)
        return shuffl

    index = shuffleindex(len(alist))
    res = []
    for idx in index:
        res.append(alist[idx])
    return res


#Sort a list by its anagrams
#iterate within a map for k, v in map.items()
# iterate only on keys :  for k in map
from listarraysalgos import qsort
def sortanagrams(words):
    # map [anagram -> list( word))
    anagramtowords= dict()
    for word in words:
        key = ''.join(sorted(word)) #from list to string representation
        if key not in anagramtowords:
            anagramtowords[key] = [word]
        else:
            anagramtowords[key].append(word)
    #return a list of sorted anagrams
    res = []
    for key, values in anagramtowords.items():
        for vit in values:
            res.append(vit)
    return res

if __name__ == "__main__":
    print('toto')
    alist = [1,2,3,4,5,6,7,8,9,10]
    res = randomshuffle(alist)
    print(res)
    mylistsort = qsort(res)
    print(mylistsort)
    mystringtosort = 'blaflakfkfzfo'
    if 'a'<'b':
        print('True')
        print( list(mystringtosort))
        print(map(lambda x: x, mystringtosort ))
    mystringsorted = qsort(list(mystringtosort))
    prefix = ''
    for c in  mystringsorted:
        prefix+=c
    print(prefix)
    alist = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    idx = bsearchrotated(alist, 0, len(alist)-1, 9)
    print(idx)


#tips : for arrays sort, search thlnk of divide and conquer approach