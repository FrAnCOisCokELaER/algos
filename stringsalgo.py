# palindrome
def ispalindrome(word):
    if len(word) == 1 or len(word) == 0:
        return True
    if word[0] != word[len(word) - 1]:
        return False
    else:
        return ispalindrome(word[1:(len(word) - 1)])
# Given a list of strings give the sub-list of all anagrams.
#
# def occurence(word): # return dict({ 'char' -> nbroccurence})
#     adict = dict()
#     for c in word:
#         occ = word.count(c)
#         adict[c] = occ
#     return adict
#
# #combinatory problem :
# def generateanagrams(occurences):
#     res = []
#
# def workfromoccurence(occurence):
#     for item in occurence:

#count method for strings can be useful : number of occurence of a character
#for sublist anagram : number of possibilities if n parmis n = n!
def permutation(word):
    def loop(prefix, word, acc):
        if not word:
            # print(prefix)
            acc.append(prefix)
        else:
            size = len(word)
            for idx in range(0, len(word)):
                loop(prefix + word[idx], word[0:idx] + word[idx + 1:], acc)

    acc = []
    loop('', word, acc)
    return acc


if __name__ == "__main__":
    word = "bonjour"
    print(ispalindrome('abcdcba'))
    res = permutation('bonjour')
    print(len(res))
