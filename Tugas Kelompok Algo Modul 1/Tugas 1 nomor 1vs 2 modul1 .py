def isPalindrome(s):
  if len(s) <= 1: #base case
    return True
  else: #recursive case
    return s[0] == s[-1] and isPalindrome (s[1:-1])

print(isPalindrome([1,2,3,4,3,2,1]))

