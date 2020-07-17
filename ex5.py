number_to_choose=int(input('please eenter a number'))
list_of_divisors=[]
for divisors in range(1,number_to_choose+1):
 if number_to_choose%divisors==0:
    list_of_divisors.append(divisors)
print(list_of_divisors)
