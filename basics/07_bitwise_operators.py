# GFG

a = int(input())
b = int(input())
c = int(input())

# XOR (^) returns 0 when both bits are the same
# Any number XOR itself is always 0
d = a^a
e = c^b 
f = a&b  # AND (&) returns 1 only when both corresponding bits are 1
g = ~e # NOT (~) inverts all the bits of a number. In Python, ~n is equivalent to -(n + 1)

print(d, e, f, g)
