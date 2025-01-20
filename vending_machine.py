import random
import os

price = {"coke":3, "pepsi":2, "mountain dew": 5, "nescafe": 3, "karak tea": 2, "nestle hot choco": 5, "lays": 2, "doritos": 4, "cheetos": 3}
items = {"A1":"coke", "A2":"pepsi", "A3": "mountain dew", 
         "B1": "nescafe", "B2": "karak tea", "B3": "nestle hot choco", 
         "C1": "lays", "C2": "doritos", "C3": "cheetos"}
stock = {"A1":(random.randint(1,6)), "A2":(random.randint(1,6)), "A3":(random.randint(1,6)), 
         "B1":(random.randint(1,6)), "B2":(random.randint(1,6)), "B3":(random.randint(1,6)),
         "C1":(random.randint(1,6)), "C2":(random.randint(1,6)), "C3":(random.randint(1,6))}
# Generates a random stock for each item which ranges from 1-6 stocks.
category = {"cold":["A1", "A2", "A3"], "hot":["B1", "B2", "B3"], "snacks":["C1", "C2", "C3"]}
# Categorizes all cold drinks, hot drinks, and snacks to improve user experience.
purchased = {}
pq = {}

def display():
    display = f"""\nCold Drinks:\nA1: {items['A1'].capitalize()}       {price['coke']} Aed| In Stock: {stock['A1']}
A2: {items['A2'].capitalize()}      {price['pepsi']} Aed| In Stock: {stock['A2']}
A3: {items['A3'].capitalize()}     {price['mountain dew']} Aed| In Stock: {stock['A3']}

Hot Drinks:\nB1: {items['B1'].capitalize()}     {price['nescafe']} Aed| In Stock: {stock['B1']} 
B2: {items['B2'].capitalize()}        {price['karak tea']} Aed| In Stock: {stock['B2']}
B3: {items['B3'].capitalize()}  {price['nestle hot choco']} Aed| In Stock: {stock['B3']}

Snacks:\nC1: {items['C1'].capitalize()}       {price['lays']} Aed| In Stock: {stock['C1']}
C2: {items['C2'].capitalize()}     {price['doritos']} Aed| In Stock: {stock['C2']}
C3: {items['C3'].capitalize()}    {price['cheetos']} Aed| In Stock: {stock['C3']}\n"""
    print(display)
    
balance = int(input("Please ennter how much money you want to insert: "))
more = "Y"
choice = None

while balance > 0 and more == "Y":
    print("\n=== VENDING MACHINE ===")
    display()
    print(f"Your balance is: {balance} AED")
    
    while True:
        spend = float(input("Enter amount to spend: "))
        if spend > balance:
            print("Insufficient funds")
        else:
            break
    
    balance = balance - spend
    while choice not in items or stock[choice]<=0:
        # Checks if the code is valid or if the item has stock.
        choice = input("Enter code: ").upper()
        if choice not in items:
            print("Enter a valid code")
        elif stock[choice]<=0:
            print("That item is out of stock") 
   
    while True:
        quantity = int(input("Enter quantity: "))
        if quantity > stock[choice]:
            # Checks if item has enough stock for quantity purchased.
            print("Not enough stock for that quantity\n")
            
        elif spend < price[items[choice]] * quantity: 
            # Checks if user has enough money for quantity.
            if spend < price[items[choice]]:
                break
            else:
                for x in range(quantity-1, 0, -1): 
                    # Goes through the prices of the item at different quantities
                    q = price[items[choice]] * x
                    if spend >= q: 
                        # Checks maximum quantity user can buy of the chosen item
                        print(f"Only {x} of that item can be purchased with your inserted money\n")
                        break
                
        else:
            break       
    if spend >= price[items[choice]] * quantity:
        change = round(spend - (price[items[choice]]) * quantity,1)
        balance = balance + change
        stock[choice] -= quantity

        print("")
        for x in range(quantity):
            print(f"|{items[choice].upper()}| DISPENSED")
        print(f"Your change is: {change} AED")
        more = input("\nBuy more items? Y/N:  ").upper()

        if items[choice] not in purchased: 
            # Adds item and quantity
            purchased.update({items[choice]:items[choice]})
            pq.update({items[choice]:quantity})
        else: 
            # Adds only quantity
            pq[items[choice]] += quantity
            
        choice = None
        os.system('cls')
        
    else:
        print(f"\nInsufficient funds")
        balance = balance + spend
        choice = None
        input("\nPress a key to return to menu")
print("\nThank you for your purchase!\n\nYou item/s:")
for x in purchased: 
# Iterate through purchased items
    for p in pq.keys(): 
    # Iterate through keys of purchased items quantity
        if p == x: 
        # Checks if quantity and item are connected via key
            print(f"{pq[p]} {x.capitalize()}(s)") 
            #Prints quantity and item