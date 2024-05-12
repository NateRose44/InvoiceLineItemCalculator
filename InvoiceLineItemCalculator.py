#Roseburrow_CIS261_InvoiceLineItemCalculator
print("Item\tPrice\tQuantity\tTotal")
print("----------------------------------")
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid price. Please enter a valid float value.")
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid quantity. Please enter a valid integer value.")
while True:
    price = get_price()
    quantity = get_quantity()
    total = price * quantity
    print(f"${price:.2f}\t{quantity}\t\t${total:.2f}")
    choice = input("Enter another line item? (y/n): ")
    if choice.lower() != 'y':
        break

