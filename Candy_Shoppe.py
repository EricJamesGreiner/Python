candy = {
  "m&m":1.99,
  "butterfinger":1.25,
  "skittles":2.99,
  "snickers":1.30
}
inventory = [5,10,2,3]
total_bill = 0

mnmQty = int(input("How many bags of M&M's?: "))

if mnmQty <= inventory[0]:
    total_bill += mnmQty * candy["m&m"]
    inventory[0] -= mnmQty
 
else:
    print("Sorry, we don't have that many M&M's! We can give you " + str(inventory[0]) + " instead.\n")
    inventory[0] = 0

butterQty = int(input("How many Butterfingers?: "))

if butterQty <= inventory[1]:
    total_bill += butterQty * candy["butterfinger"]
    inventory[1] -= butterQty
else:
    print("Sorry, we don't have that many Butterfingers! We can give you " + str(inventory[1]) + " instead.\n")
    inventory[1] = 0  

skittlesQty = int(input("How many bags of Skittles?: "))

if skittlesQty <= inventory[2]:
    total_bill += skittlesQty * candy["skittles"]
    inventory[2] -= skittlesQty
else:
    print("Sorry, we don't have that many Skittles! We can give you " + str(inventory[2]) + " instead.\n")
    inventory[2] = 0  

snickersQty = int(input("How many Snickers?: "))

if snickersQty <= inventory[3]:
    total_bill += snickersQty * candy["snickers"]
    inventory[3] -= snickersQty
else:
    print("Sorry, we don't have that many Snickers! We can give you " + str(inventory[3]) + " instead.\n")
    inventory[3] = 0  


print("\nThanks for the order....")
print(f"Your cost will be ${total_bill:2.2f}")