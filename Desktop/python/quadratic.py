import cmath
print("Enter the values of a,b,c :")
a=int(input())
b=int(input())
c=int(input())
d=(b**2)-(4*a*c)
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are:")
    print(f"root1 = {root1:.1f}")
    print(f"root2 = {root2:.1f}")
elif d == 0:
    root = -b / (2*a)
    print("The roots are:")
    print(f"root1 = {root:.1f}")
    print(f"root2 = {root:.1f}")
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(d)) / (2*a)
    print("The roots are:")
    print(f"root1 = {real_part:.1f}")
    print(f"root2 = {real_part:.1f}")
