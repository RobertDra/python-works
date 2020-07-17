a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
num2 = int(input('enter a number'))
for num in a:

    if num < num2:
        newlist.append(num)
print(newlist)