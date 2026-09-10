a=int(input("Enter side 1 :-"))
b=int(input("enter side 2 :-"))
c=int(input("enter side 3 :-"))
if a+b>c and b+c>a and c+a>b:
    print("Valid Triangle")
else:
    print("not a valid triangle")