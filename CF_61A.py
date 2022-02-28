import numbers


number_1 = input()
number_2 = input()
add_two_number = ""
for i in range(len(number_1)):
    if number_1[i] == '1' and number_2[i] =='0':
        add_two_number += '1'
    elif number_1[i] == '0' and number_2[i] =='1':
        add_two_number += '1'
    else:
        add_two_number += '0'
print(add_two_number)
        
