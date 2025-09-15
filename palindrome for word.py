text = input("Enter a word or phrase: ")
cleaned = text.replace(" ", "")
if cleaned == cleaned[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")