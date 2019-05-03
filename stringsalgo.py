def ispalindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    if word[0] != word[len(word) - 1]:
        return False
    else:
        return ispalindrome(word[1:(len(word) - 1)])


if __name__ == "__main__":
    word = "toto"
    print(ispalindrome('abcdcba'))
