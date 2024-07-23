import cmath
a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
d = (b**2)-(4*a*c)
rot1 = (-b-(cmath.sqrt(d)))/2*a
rot2 = (-b+(cmath.sqrt(d)))/2*a
print("root1 is {0} \n root2 is {1}".format(rot1,rot2))
