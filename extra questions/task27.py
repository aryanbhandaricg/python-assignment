hours = int(input("Enter hours"))
min = int(input("Enter minutes"))
sec= int(input("Enter seconds"))

if 0<= hours <= 23 and 0<= min <= 59 and 0<= sec <= 59:
    print("Valid Time")
else:
    print("Invalid Time")