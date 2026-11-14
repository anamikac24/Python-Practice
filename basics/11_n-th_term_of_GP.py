#GFG 
#Problem: N-th Term of a GP (Geometric Progression)

class Solution:
    def nthTerm(self, a, r, n):
        
        # A Geometric Progression (GP) is a sequence in which
        # each term is obtained by multiplying the previous term
        # by a constant called the common ratio (r).

        # Formula for the N-th term:
        # Tn = a * r^(n-1)
        # a = First term
        # r = Common ratio
        # n = Position of the term

        # We use modulo 10^9 + 7 because the result can be very large.
        mod = 1000000007

        # pow(r, n-1, mod) calculates r^(n-1) % mod efficiently.
        # Finally, multiply by the first term and take modulo again.

        return (a * pow(r, n-1, mod)) % mod
