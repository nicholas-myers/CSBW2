def isPalindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    # remove all the punctiation and spacing
    original = [c.lower() for c in s if c.isalnum()]
    # save the chars in the current order
    original_str = "".join(str_list)
    print(original)
    # reverse the chars
    str_list.reverse()
    print(str_list)
    reverse = "".join(str_list)
    # see if reverse is equal to the orginal
    if original == reverse:
        print("this is a palindrome")
        return True
    else:
        print("this is not a palindrome")
        return False
        
isPalindrome("A man, a plan, a canal: Panama")
isPalindrome("race a car")
