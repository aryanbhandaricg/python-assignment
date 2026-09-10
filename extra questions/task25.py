s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))

if s1 < 0 or s1 > 100 or s2 < 0 or s2 > 100 or s3 < 0 or s3 > 100:
    print("Invalid marks")
elif s1 < 35 or s2 < 35 or s3 < 35:
    print("Fail")
else:
    average = (s1 + s2 + s3) / 3
    print(f"Average:{average}")

    if average >= 75:
        print("Distinction")
    elif average >= 60:
        print("First Class")
    elif average >= 50:
        print("Second Class")
    else:
        print("Pass")