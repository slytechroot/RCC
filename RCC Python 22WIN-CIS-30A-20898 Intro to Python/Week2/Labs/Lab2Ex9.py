"""9.Given the string: “No pain, no gain!?!”.
Write a Python program that uses replace() to remove all
the punctuations from the given string. Hint: Use for and if statements.
"""

strng = "No pain, no gain!?!"
punc = ",!?!;:"

for ch in strng:
    if ch in punc:
        strng = strng.replace(ch, "")
        print(strng)











