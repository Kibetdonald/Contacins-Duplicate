# check if the strings are valid anagram
def checkValidAnagram():
        s = "anagram"
        t = "nagaram"
        #  if statement to check length
        if len(s) != len(t):
            return False
        elif sorted(s) == sorted(t):
            return True
        else:
            return False
print(checkValidAnagram())
