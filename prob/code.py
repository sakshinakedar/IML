import fractions
x = 5*['w'] + 4*['b']
y = 7*['w'] + 6*['b']
xw = x.count('w')
xb = x.count('b')
total = 0
counter = 0
while len(x) != 0:
    ball = x.pop()
    y.append(ball)
    total += len(y)
    counter += y.count('b')
    y.pop()

a = counter/total
x = fractions.Fraction(a).limit_denominator(100)
print(x)
