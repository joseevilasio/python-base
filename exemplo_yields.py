

list_compr = [x for x in range(10)]
print(list_compr)
# >> [0, 1, 2, 3, 4, 5, 6, 7, 9, 10]

list_gener = (x for x in range(10))
print(next(list_gener))
# >> <generator object <genexpr> at 0x7fcd403145c8>
