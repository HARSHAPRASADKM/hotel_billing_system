menu = {
    "dosa": 40,
    "tea": 10,
    "coffee": 15,
    "idli": 20,
    "vada_pav": 25
}

ordered_items = {}

total_bill = 0
discount_percent = 0
discount_amount = 0
final_bill = 0

print("----- Welcome to College Canteen -----")
print("\nMenu:")
for item, price in menu.items():
    print(f"{item} -> ₹{price}")

while True:
    item_name = input("\nEnter item name (or type 'q' to finish): ").lower()

    if item_name == "q":
        break

    if item_name not in menu:
        print("Item not in menu. Try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if item_name in ordered_items:
        ordered_items[item_name] += quantity
    else:
        ordered_items[item_name] = quantity

print("\n----- BILL DETAILS -----")
for item, qty in ordered_items.items():
    price = menu[item]
    item_total = price * qty
    total_bill += item_total
    print(f"{item} x {qty} = ₹{item_total}")

if total_bill > 500:
    discount_percent = 20
elif total_bill > 200:
    discount_percent = 10
else:
    discount_percent = 0

discount_amount = (total_bill * discount_percent) / 100
final_bill = total_bill - discount_amount

print("\n---------------------------")
print("Total Bill:", total_bill)
print(f"Discount ({discount_percent}%):", discount_amount)
print("Final Bill to Pay:", final_bill)
print("---------------------------")
print("Thank you! Visit Again 😊")
