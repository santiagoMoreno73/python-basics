# # print console
# print()
# # more info
# dir()
# # type 
# type()

# functions
def hello(name = 'Person'):
    print("Hello", name) 

hello('Fazt')
hello('Santiago')
hello('Nana')
hello('')

def add(a1, a2): 
    return a1 + a2

print(add(10, 30))
print(add(120, 220))

# lambda functions 
add = lambda n1, n2: n1 + n2
print(add(20, 30))
