# Palindrome text checking ...Given text is palindrome or not..

text = input("Please enter the Value or Number :")
New = text[::-1]
print(New)
if New==text:
    print("The text is Palindrome ",text)
else:
    print("The text is not palindrome",text)
