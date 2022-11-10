def isPalindrome(data: str) -> str:
    dataNew = ''.join(letter.lower() for letter in data if letter.isalnum())
    print(f"'{data}' is palindrome" if dataNew == ''.join(reversed(dataNew)) else f"'{data}' isn`t palindrome")


#isPalindrome('Eva, can I see bees in a cave')
isPalindrome('Madam')
