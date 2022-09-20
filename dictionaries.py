product = {
    "name": "book",
    "quantity": 3,
    "price": 4.99 
}

person = {
    "first_name": "Erick",
    "last_name": "Ray"
}

print(type(product))
# get keys 
print(product.keys())
# get items
print(product.items())

# clear 
person.clear()
print(person)
# delete
# del person
# print(person)

products = [
    {"name": "Book", "price": 10.99 },
    {"name": "Pencil", "price": 10.29 }
]

print(type(products))