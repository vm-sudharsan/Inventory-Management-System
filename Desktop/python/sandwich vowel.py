def isVowel(x):
    if (x == 'a' or x == 'e' or x == 'i' or
                    x == 'o' or x == 'u'):
        return True
    else:
        return False

def updateSandwichedVowels(a):
    n = len(a)
    updatedString = ""
    for i in range(0, n, 1):
      if (i == 0 or i == n - 1):
        updatedString += a[i]
        continue
      if (isVowel(a[i]) == True and
            isVowel(a[i - 1]) == False and
            isVowel(a[i + 1]) == False):
            continue
      updatedString += a[i]
    return updatedString

# Main block
str = "vowel"
# Remove all the Sandwitched Vowels
updatedString = updateSandwichedVowels(str)
print(updatedString)
