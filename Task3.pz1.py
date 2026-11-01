sales = [
    {"product": "bread", "quantity": 15, "price": 20},
    {"product": "pack of spagetti", "quantity": 30, "price": 47},
    {"product": "pack of sausages", "quantity": 23, "price": 57}]

def total_income(sales_list):
    income_dict = {}
    for item in sales_list:
        product_name = item["product"]
        income = item["quantity"] * item["price"]
        if product_name in income_dict:
            income_dict[product_name] += income
        else:
            income_dict[product_name] = income
    return income_dict

result_income = total_income(sales)
print("Total income:\n", result_income)

hight_income_product = []
for product, income in result_income.items():
    if income > 1000:
        hight_income_product.append(product)
print("\nProducts with revenue over 1000: ",hight_income_product)