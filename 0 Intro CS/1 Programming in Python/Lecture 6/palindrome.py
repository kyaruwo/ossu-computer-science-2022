def isPalindrome(word):
    word = word.lower().translate(
        {ord(c): None for c in " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"})
    return word == word[::-1]


print(isPalindrome("Able was I, ere I saw Elba"))


# https://pythontutor.com/visualize.html#code=def%20isPalindrome%28word%29%3A%0A%20%20%20%20word%20%3D%20word.lower%28%29.translate%28%0A%20%20%20%20%20%20%20%20%7Bord%28c%29%3A%20None%20for%20c%20in%20%22%20!%5C%22%23%24%25%26'%28%29*%2B,-./%3A%3B%3C%3D%3E%3F%40%5B%5C%5D%5E_%60%7B%7C%7D~%22%7D%29%0A%20%20%20%20return%20word%20%3D%3D%20word%5B%3A%3A-1%5D%0A%0A%0Aprint%28isPalindrome%28%22Able%20was%20I,%20ere%20I%20saw%20Elba%22%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
# comparison
# https://pythontutor.com/visualize.html#code=def%20recursive_isPalindrome%28word%29%3A%0A%0A%20%20%20%20def%20parseString%28s%29%3A%0A%20%20%20%20%20%20%20%20ns%20%3D%20%22%22%0A%20%20%20%20%20%20%20%20from%20string%20import%20ascii_lowercase%20as%20letters%0A%20%20%20%20%20%20%20%20for%20c%20in%20s.lower%28%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20c%20in%20letters%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20ns%20%2B%3D%20c%0A%20%20%20%20%20%20%20%20return%20ns%0A%0A%20%20%20%20def%20isPalindrome%28s%29%3A%0A%20%20%20%20%20%20%20%20if%20len%28s%29%20%3C%202%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20True%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20s%5B0%5D%20%3D%3D%20s%5B-1%5D%20and%20isPalindrome%28s%5B1%3A-1%5D%29%0A%0A%20%20%20%20return%20isPalindrome%28parseString%28word%29%29%0A%0A%0Aprint%28recursive_isPalindrome%28%22Able%20was%20I,%20ere%20I%20saw%20Elba%22%29%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


def recursive_isPalindrome(word):

    def parseString(s):
        ns = ""
        from string import ascii_lowercase as letters
        for c in s.lower():
            if c in letters:
                ns += c
        return ns

    def isPalindrome(s):
        if len(s) < 2:
            return True
        else:
            return s[0] == s[-1] and isPalindrome(s[1:-1])

    return isPalindrome(parseString(word))


print(recursive_isPalindrome("Able was I, ere I saw Elba"))
