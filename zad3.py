from decimal import *

def generate (first , last):
    first = Decimal(first)
    last = Decimal(last)
    generated = []
    while(first<=last):
        generated.append(first)
        first = first + Decimal(0.5)
    return generated
print(generate(2.0,5.5))
