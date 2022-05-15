def isWordPresent(sentence, word):
    # To break the sentence in words
    s = sentence.split(" ")
    for i in s:

        if (i == word):
          return True
    return False
s = "what is your name"
word = "name"

if (isWordPresent(s, word)):
    print("Yes")
else:
    print("No")