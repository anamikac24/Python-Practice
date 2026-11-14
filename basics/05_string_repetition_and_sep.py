# GFG
# Given three inputs a,b and c. Print a exactly a times and b exactly b times with c between them.
# For string repetition - str*number.

a = input()
b = input()
c = input()

print(a*int(a), b*int(b), sep=c) # a*int(a) - repeats a as many times as it's own numeric value.

