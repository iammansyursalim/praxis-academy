numbers = [13, 4, 18, 35]
div_by_5 = filter(lambda num: num % 5 == 0, numbers)

# We can convert the iterator into a list
print(list(div_by_5)) # [35]