odd_numbers = [1,3,5,7,9]
even_numbers = [0,2,4,6,8]

unified_list = odd_numbers + even_numbers
new_list = []

for i in unified_list:
    i *= 2
    new_list.append(i)

for j in new_list:
    print(type(j))