from fractions import Fraction

answer = Fraction(1, 100)
for i in range(2, 100):
    j = 101 - i
    a = Fraction(1, i + 1)
    b = Fraction(1, j)
    answer += float(a) * float(b)

print(a)
print(b)
print(answer * 100)