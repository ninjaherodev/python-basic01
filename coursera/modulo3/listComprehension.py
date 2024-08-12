numbers = []
for element in range(1,11):
    if(element % 2 == 0):
        numbers.append(element * 2)
print(numbers)

#List Comprehension

numbers_lc = [element * 2 for element in range(1,11) if element % 2 == 0]
print(numbers_lc)