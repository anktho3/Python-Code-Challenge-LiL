import re
def palindrome(palString):
    palCheck = str(palString.strip().lower())
    palCheck = re.sub  (r'[^a-z]', '', palCheck)
    RevpalCheck = palCheck[::-1]
    return palCheck == RevpalCheck

while True:
    print(palindrome(input("Enter word: ")))