num=int(input("Enter number to check range:- "))
if num<0:
    print("Negative")
elif num<=10:
    print("No. is btw 0-10")
elif num<=50:
    print("No. is btw 11-50")
elif num<=100:
    print("No. is btw 51-100")
else:
    print("Above 100")