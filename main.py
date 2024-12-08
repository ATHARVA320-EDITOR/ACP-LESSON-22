test_dict = {'Hello': 4, 'I': 1, 'am': 1, 'Atharva': 3, 'Kumar': 3}
value = str(input("Enter value to see frequency: "))
print(value)
value2 = int(input("Enter the value you want for Frequency: "))
print(value2)
Frequency = value2
res = 0
for key in test_dict:
    if test_dict[key] == Frequency:
        res = res + 1
print("Frequency of  the value is :" + str(res))