foods = ['apples', 'graves', 'bananas', 'bread', 'cheese', 'milk']

for food in foods:
    if food == "cheese":
        print("you have to buy this")
        break
    print(food)
 
for food in foods:
    if food == "cheese":
        continue
    print(food)

for number in range(1, 8): 
    print(number)

for letter in "Hello":
    print(letter)

count = 4 

while count <= 10:
    print(count)
    count = count + 1
    