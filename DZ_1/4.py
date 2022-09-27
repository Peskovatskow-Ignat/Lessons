x=int(input())
y=int(input())
z=int(input())
print(x+y+z)
if x>y and x>z:
    print(x)
elif y>x and y>z:
    print(y)
else:
    print(z)
if x<y and x<z:
    print(x)
elif y<x and y<z:
    print(y)
else:
    print(z)