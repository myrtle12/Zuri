# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(first_string, Second_string):
    # [assignment] Add your code here
  if sorted(first_string) == sorted(Second_string):
    return True
  else:
     return False
find_anagrams("life", "file")
