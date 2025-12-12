numbers = [1,2,3,4,5,6,7,8,9]
result = []

for number in numbers:
    if (number % 2 == 0):
        result.append(number)

result = [number for number in numbers if number % 2 == 0]
print(result)


# new example

price_of_products = [1000,990,549,220]
result = []

for product in price_of_products:
    if product > 400:
        result.append(product)
    

    result = [product for product in price_of_products if product > 400 ]
    print(result)