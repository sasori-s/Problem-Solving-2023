def checkPalindrome(word, start, end):
    if start >= end:
        return 1
    
    if word[start] != word[end]:
        return 0
    
    return checkPalindrome(word, start + 1, end - 1 )

if __name__ == "__main__":
    word = "abba"
    n = len(word) - 1

    if checkPalindrome(word, 0, n):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")