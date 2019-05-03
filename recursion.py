import unittest

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

    def test_pascel(self):
        self.assertEqual(pascaltriangle(1,3), 3)

    def test_balance(self):
        expr = '(if (zero? x) max (/ 1 x))'
        self.assertTrue(balance(expr))
    def test_balance2(self):
        expr = ':-)'
        self.assertFalse(balance(expr))
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == "__main__":
    #print(pascaltriangle(1,3))
    unittest.main()
    balance("toto")