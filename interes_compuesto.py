from decimal import Decimal, ROUND_HALF_UP

p = Decimal('10000.00')
r = Decimal('0.05')
n = Decimal('10')

c=r+1
c = c**n
c=p*c

c = c.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print(f"c = p(1+r)^n c = {p} (1 {r})^{n}")
print(f"c = {c}")