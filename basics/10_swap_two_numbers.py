# GFG

#First approach
a = int(input())
b = int(input())

temp = b   # We use a third variable to store one of variables temporary.
b = a
a = temp

print(a,b, end='')

#Second approach
a = int(input())
b = int(input())

a,b=b,a

print(a,b, end='')
