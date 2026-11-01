products = {"pasta": 20,
            "potatoes": 47,
            "cucumbers": 25,
            "oranges": 33,
            "oatmeal": 17,
            "yogurts": 39}
print("Products:")
for key, value in products.items():
    print(key, ":", value)

def update_inventory(products_name, number):
    if products_name in products:
        products[products_name] += number
    else:
        products[products_name] = number

update_inventory("pasta", +3)
update_inventory("potatoes", -43)
update_inventory("yogurts", -5)
update_inventory("oranges", +11)
update_inventory("oatmeal", -13)
update_inventory("apples", 21)
update_inventory("bread", 45)

print("---------------------")
print("Updated inventory:")
for key, value in products.items():
    print(key, ":", value)

smaller_quantity = []
for item, count in products.items():
    if count < 5:
        smaller_quantity.append(item)
print("\nProducts with smaller quantity:", smaller_quantity)
