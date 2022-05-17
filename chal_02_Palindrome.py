import re
def palindrome(palString):
    palCheck = str(palString.strip().lower())
    palCheck = re.sub  (r'[^a-z]', '', palCheck)
    RevpalCheck = palCheck[::-1]
    if RevpalCheck == palCheck:
        return True
    else:
        return False

while True:
    print(palindrome(input("Enter word: ")))