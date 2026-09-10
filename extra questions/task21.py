a=int(input("Enter side 1 :-"))
b=int(input("enter side 2 :-"))
c=int(input("enter side 3 :-"))
if a+b>c and b+c>a and c+a>b:
    print("Valid Triangle")
    if a==b and b==c:
      print("Equilateral")
    elif a==b or b==c or c==a:
     print("Isosceles")
    else:
     print("Scalene")
else:
    print("not a valid triangle")