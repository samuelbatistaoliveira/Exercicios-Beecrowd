a,b,c = map(float,input().split())

if (a < b + c) and (b < a + c) and (c < a + b):
    Perimetro = a + b + c
    print(f"Perimetro = {Perimetro:.1f}")
else:
    Area = ((a + b) * c) /2
    print(f"Area = {Area:.1f}")