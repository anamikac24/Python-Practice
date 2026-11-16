# GFG
# Problem: Given a string s, return a string containing all characters present at even indices. 
# Concept: String Traversal using a while loop and indexing.

s = input("enter a word: ")

result="" # Initializing an empty string to store the result.

i=0
while i<len(s):
    result+=s[i]  # Adding the character at the current index to result.
    i+=2   # Incrementing the index by 2 to skip every alternate character.

print(result)
