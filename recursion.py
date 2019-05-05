import unittest
import math

#compute the gcd of a and b
#euclidean algorithm
#explanation let a = bq+r then id gcd divide a and b it also divides b and b*q + r so it should divide r
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def isprime(n, i=2):  # si N = pq i.e. pas premier alors soit p ou q < sqrt(N)
    if n==2 or n==1:
        return True
    if n%i is 0:
        return False
    elif (i*i)>n: # true because all possible combination for i has been done
        return True
    else:
        return isprime(n,i+1)

#pascal triangle
def pascaltriangle(col, row):
    if col == 0 or col == row:
        return 1
    else:
        return pascaltriangle(col-1, row-1)+pascaltriangle(col, row-1)

#factorial
def factorial(n):
    if n is 0:
        return 1
    else:
        return n*factorial(n-1)

#find if a string is balanced
def isbalanced(count, anexpression):
    if len(anexpression) is 0:
        if count == 0:
            return True
        else:
            return False
    else:
        if anexpression[0] == '(':
            count += 1
        elif anexpression[0] == ')':
            count -= 1
        return (isbalanced(count, anexpression[1:]))

def balance(expression):
     return isbalanced(0, expression)

#recursion for combinatorial problem
def countChange(money, coins):
    if money ==0:
        return 1
    elif money <0 or (len(coins) is 0):
        return 0
    else:
        return countChange(money-coins[0], coins) + countChange(money, coins[1:])


class TestRecusrion(unittest.TestCase):

    def test_pascal(self):
        self.assertEqual(pascaltriangle(1,3), 3)
    def test_balance(self):
        expr = '(if (zero? x) max (/ 1 x))'
        self.assertTrue(balance(expr))
    def test_balance2(self):
        expr = ':-)'
        self.assertFalse(balance(expr))

if __name__ == "__main__":
    #print(pascaltriangle(1,3))
    #unittest.main()
    balance("toto")
    print(gcd(75,25))
    print(isprime(7))