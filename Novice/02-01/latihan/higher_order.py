def write_repeat(message, n):
    for i in range(n):
        print(message)

write_repeat('Hello', 5)

print()

def hof_write_repeat(message, n, action):
    for i in range(n):
        print(message)

hof_write_repeat('Hello', 5, print)

#import library logging
import logging

#log the output as an error instead
hof_write_repeat('hello', 5, logging.error)

print()

def add2(numbers):
    new_numbers = []
    for n in numbers:
        new_numbers.append(n + 2)
    return new_numbers
print(add2([23,88]))

print()
print('MENGGUNAKAN High Order Functions')
print()

def hof_add(increment):
    #create a function that loops and adds the increment
    def add_increment(numbers):
        new_numbers = []
        for n in numbers:
            new_numbers.append(n + increment)
        return new_numbers
    return add_increment

add5 = hof_add(5)
print(add5([23,88]))
add10 = hof_add(10)
print(add10([23,88]))