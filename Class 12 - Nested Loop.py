print("ATM CASH DISPENSER\n")
total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
money_dispensed = 0
serving = True
while serving:
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}, enter withdrawal amount: "))
    if amount <= 0:
        print("ERORR. Invalid amount!\nEnter valid amount.\n")
        continue
    print(f"Dispensing ${amount} for user {name}: ")
    remaining = amount
    idx = 1
    while idx <= 6:
        if idx == 1: value = 100
        elif idx == 2: value = 50
        elif idx == 3: value = 20
        elif idx == 4: value = 10
        elif idx == 5: value = 5
        else: value = 1
        count = remaining // value
        if count > 0:
            print(f"{count} X ${value} note(s) = {count*value}")
            remaining -= count * value
            if value == 100: total_100 += count
            elif value == 50: total_50 += count
            elif value == 20: total_20 += count
            elif value == 10: total_10 += count
            elif value == 5: total_5 += count
            elif value == 1: total_1 += count
            else: print("ERORR. Please enter whole number.")
        idx += 1
    customers_served += 1
    money_dispensed += amount
    print("Transaction complete,", name,"\n")
    again = input("Next customer (yes/no): ").strip().lower()
    if again != "yes":
        serving = False
print("\nCustomers served: ",customers_served)
print("Total dispensed: $",money_dispensed)
print("ATM session complete. Thank you.")