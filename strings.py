myStr = "Hello World"

# see methods with dir 
# print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())

print(myStr.replace("Hello", "Hi").upper())
print(myStr.count("l"))
print(myStr.startswith("Hello"))
print(myStr.endswith("Word"))

# separate default space
print(myStr.split())
# separato with letter O
print(myStr.split("o"))

# search letter, resp the position 
print(myStr.find("o"))

# longitud
print(len(myStr))

print(myStr.index("e"))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])

print("My name is " + myStr)
print("My name is {0}".format(myStr))

# available with version 3.6 up 
print(f"My name is {myStr}")