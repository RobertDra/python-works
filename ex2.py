x = input('Enter your name:')
print('Hello, ' + x)
y = int(input('what year it is?'))
z = int(input('how old are u?'))
def calculate(y, z):
    return y-z+100

print('you will be 100 years old at',calculate(y, z))