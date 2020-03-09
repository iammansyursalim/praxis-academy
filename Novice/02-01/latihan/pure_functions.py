dictionary = ['fox','boss','orange','toes','fairy','cup']
def pluralize(words):
    result = []
    for word in words:
        word = words[i]
        if word.endswith('s') or word.endswith('x'):
            plural = word + ('es')
        if word.endswith('y'):
            plural = word[:-1] + 'ies'
        else:
            plural =+ 's'
        result.append(plural)
        return result
def test_pluralize():
    result = pluralize(dictionary)
    assert result == ['foxes','bosses','oranges','toeses','fairies','cups']

print()

def multiply_2_pure(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n * 2)
    return new_numbers

original_numbers = [1, 3, 5, 10]
changed_numbers = multiply_2_pure(original_numbers)
print(original_numbers) # [1, 3, 5, 10]
print(changed_numbers)  # [2, 6, 10, 20]