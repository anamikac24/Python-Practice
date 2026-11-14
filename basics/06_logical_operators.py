# GFG
# input(): This captures what is typed into the console as a string (text), rather than a boolean value.

# strip(): This removes any accidental leading or trailing whitespace (spaces or tabs) from the input string to ensure clean comparison.

# lower(): This converts the entire string to lowercase (e.g., changing "True", "TRUE", or "true" to "true"), preventing case-sensitivity errors.

# == "true": This compares the cleaned lowercase string against the literal string "true".
# If they match, it evaluates to the boolean True; otherwise, it evaluates to False.

x = input().strip().lower() == "true"
y = input().strip().lower() == "true"

p = x and y
q = x or y
r = not x
s = not y

print(p, q, r, s)
