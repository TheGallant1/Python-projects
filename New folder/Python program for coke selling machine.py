
total = 0
due = 50
coins = [25, 10, 5]
Amount_due = 0

while total < due:
    Amount_due = due - total
    print("Amount due: ", Amount_due,"Cents")
    coin = int(input("Insert a coin (5, 10, 25): "))

    if coin in coins:
        total += coin

change = total - due
print("Change owed:", change, "cents")
