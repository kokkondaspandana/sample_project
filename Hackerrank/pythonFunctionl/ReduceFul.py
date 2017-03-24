def product(fracs):
    t = Fraction(reduce(lambda x,y:Fraction(x*y),fracs))
    return t.numerator, t.denominator

Sample Input 

3
1 2
3 4
10 6
Sample Output 

5 8
