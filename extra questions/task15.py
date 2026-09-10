cp = float(input("Enter cost price: "))
sp = float(input("Enter selling price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
    print("Profit % =", profit / cp * 100)

elif cp > sp:
    loss = cp - sp
    print("Loss =", loss)
    print("Loss % =", loss / cp * 100)

else:
    print("No profit and no loss")