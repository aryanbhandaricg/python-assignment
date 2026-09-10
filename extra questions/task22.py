balance=7000
withdraw=float(input("Enter withdrawl amount: "))

if withdraw<=0:
    print("Invalid withdrawl amount")
elif withdraw %100 !=0:
    print("Amount must be divisible by 100")
elif withdraw>balance:
    print("Insufficient balance")
elif balance - withdraw <500:
    print("At least 500 must remain")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)