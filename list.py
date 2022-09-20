demo_list = [1 , "hello", False, 1.45, [1, 2, 4]]
colors = ["green", "blue", "nullColor", "red", "red"]

# create list with constructor
number_list = list((1, 2, 3, 4, 5))
print(number_list)
print(type(number_list))

r = list(range(1, 11))
print(r)

print(type(colors))
print(len(colors))
print("green" in colors)

# change values
colors[1] = 'Violet'
print(colors)

# methods add Elements
colors.append('violet')
colors.extend(('purple', 'yellow'))
colors.insert(1, 'gray')
colors.insert(len(colors), 'orange')

# methods delete Elements 
'''last item'''
colors.pop()
'''with index'''
colors.pop(1)
'''with name element'''
colors.remove('green')

# order Elements
colors.sort()
colors.sort(reverse=True)
print(colors.index('red'))
print(colors.count('red'))


# delete all Elements
colors.clear()