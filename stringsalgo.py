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

#check if word1 is an edit of word
#one char can be remove added of replace
def iseditof(word1, word2):
    count = 0
    if len(word1) is len(word2):
        for idx in range(0,len(word1)):
            if word1[idx] != word2[idx]:
                if count>=1:
                    return False
                count = count+1
        return True
    elif len(word2) is len(word1)-1 :
        idx1 = 0
        idx2=0
        while idx2 < len(word2):
            if word1[idx1] != word2[idx2]:
                if count >=1:
                    return False
                count+=1
                idx1 +=1
            else:
                idx1+=1
                idx2+=1
        return True
    elif len(word1) is len(word2) - 1:
        return iseditof(word2, word1)
    else:
        return False

    #same size : one char only  is replaced
    #len(word2) < len(word1)
    #len(word2) > len(word1)

#tips : wort a string : sorted(mystring)
#string - > list with split
#list - > string ''.join
#    prefix = ''
#    for c in  mystringsorted:
#        prefix+=c


#iterate within a map for k, v in map.items()
#onlyr keyds for k in map
from listarraysalgos import qsort
#group by a list by anagrams
def sortanagrams(words):
    #wordssorted = [qsort(aword.split()) for aword in words]
    # map [anagram -> list( word))
    anagramtowords= dict()
    for word in words:
        key = ''.join(sorted(word))
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
    word = "bonjour"
    print(ispalindrome('abcdcba'))
    res = permutation('bonjour')
    print(len(res))
    print(iseditof('bonjour','bonnjkur'))
    a = bytes('Hello World', encoding='utf-8')
    print('toto')
    anagramslist = ['coucou', 'salut', 'eocrit', 'cuocuo', 'lutsa', 'criteo']
    print(anagramslist)
    res = sortanagrams(anagramslist)
    print(res)