word=input("Enter your word: ")
rev = ""

for ch in word:
    rev = ch + rev   # build reverse

if word == rev:
    print("Palindrome")
else:
    print("Not Palindrome")