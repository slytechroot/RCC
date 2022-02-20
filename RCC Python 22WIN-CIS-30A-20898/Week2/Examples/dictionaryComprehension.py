#Dictionary Comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#same as above, but written differently
squares = {}
for x in range(6):
    squares[x] = x*x
print(squares)

