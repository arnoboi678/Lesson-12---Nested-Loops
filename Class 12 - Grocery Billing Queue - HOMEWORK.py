print("Grocery Biller\n")
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True

while billing:
    name = input("Enter customer name: ")
    item_count = int(input(f"Hello {name}! How many items are you purchasing? "))
    if item_count <= 0:
        print("ERROR 404. INVALID INPUT ENTERED.")
        continue
        
    print(f"\nBilling items for {name}:")
    customer_total = 0
    item_number = 1  # Reset counter to 1 for every new customer
    
    while item_number <= item_count:
        item_name = input(f"Enter item #{item_number} name: ")
        price = int(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))
        
        if price <= 0 or quantity <= 0:
            print("ERROR 404. INVALID INPUT ENTERED. Please enter price or quantity again.\n")
            continue  # Re-runs the loop for the SAME item number
            
        # Valid inputs process here
        item_total = price * quantity
        print(f" {item_name}: {quantity} x ${price} = ${item_total}.\n")
        customer_total += item_total
        
        # Categorize items into price buckets based on individual item price
        if price < 5:
            low_price_items += quantity
        elif price <= 15:
            medium_price_items += quantity
        else:
            high_price_items += quantity
            
        item_number += 1  # Move to the next item number only when successful!
        
    # Customer summary (Runs outside the item loop, after all items are added)
    print(f"\nTotal bill for {name}: ${customer_total}")
    print("Billing complete!\n")
    
    # Update global report counters
    customers_served += 1
    total_sales += customer_total
    
    # Ask about the next customer
    repeat_prompt = input("New customer? (yes/no): ").strip().lower()
    if repeat_prompt == "no":
        billing = False

# Final summary report (Runs after you type "no")
print("\nGrocery Biller Report")
for slot in range(1, 4):
    if slot == 1:
        label, total = "Low priced items   ", low_price_items
    elif slot == 2:
        label, total = "Medium priced items", medium_price_items
    elif slot == 3:
        label, total = "High priced items  ", high_price_items
        
    if total > 0:
        print(f"   {label}:    {total} ", end="")
        for star in range(total):
            print("*", end="")
        print()

print(f"Customers served : {customers_served}")
print(f"Total sales      : ${total_sales}")
print("\nThank you for using Grocery Biller. Goodbye!")
