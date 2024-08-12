squares = ['orange', 'red', 'blue']

# for i in range(len(squares)):
#     squares[i] = 'white'

# for i,square in enumerate(squares):
#     print(square)
#     squares[i] = 'white'

# print(squares)
# squares = ['orange', 'red', 'blue']
# squares[:] = ['white'] * len(squares)
# print(squares)
i = 0
while i < len(squares):
    squares[i] = 'white'
    i += 1
print(squares)
