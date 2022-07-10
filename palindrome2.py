def isPalindrome(strng):
    if len(strng)==0:
        return True
    if strng[0]!=strng[len(strng)-1]:
        return False
    return isPalindrome(strng[1:-1])
print(isPalindrome('awesome')) 
print(isPalindrome('foobar')) 
print(isPalindrome('tacocat')) 
print(isPalindrome('amanaplanacanalpanama')) 
print(isPalindrome('amanaplanacanalpandemonium')) 
