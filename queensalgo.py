# 8 queens placing problem with brute force approach
def issafe(col, queens):
    safe = True
    row = len(queens)
    for r, c in zip(range(row-1, -1, -1), queens):
        if col == c or abs(c-col) == (row-r):
            safe = False
    return safe

# 8 queens problem
def queens(n):
    def placequeens(k):
        if k ==0:
            aset = set()
            aset.add(tuple())
            return aset
        else:
            queens = placequeens(k-1)
            res = set()
            for queen in queens:
                for col in range(0, n):
                    if issafe(col, queen):
                        atuple = (col,) + queen
                        res |= set((atuple,))
            return res
    return placequeens(n+1)


# 8 queens problem
# for a set : need a hashable type : tuple
# a tuple with one element if of type of this element : need to use (myint, )
# set is a mutable type in python : user the binary operator |= to append a nex tuple to the set
# range(n-1, -1, 0) is an iterable going form n-1 to 0


if __name__ == "__main__":
    queens(4)