
print("FUNCTION GREETING")

def greeting():
    print('hello world')

greeting()

###################################
print()

print("Passing Function as Parameters")

def formalGreeting():
    print('how are you ?')

def casualGreeting():
    print("what's up?")

def greet(type,formalGreeting,casualGreeting):
    if type == 'formal':
        formalGreeting()
    elif type == 'casual':
        casualGreeting()

greet('formal',formalGreeting,casualGreeting)
print()
greet('casual',formalGreeting,casualGreeting)

#############################################
print()

print("Assigning Function to Variables")

def squares(x):
    return x * x

square = squares
print(square(5))

#############################################
print()

print("Example 1 WITHOUT High order function")

arr1 = [1,2,3]
arr2 = []

for i in arr1:
    arr2.append(i*2)
    
print(arr2)

##############################################
print()

print('Example 1 WITH High Order Function')

arr1 = [1,2,3]

arr2 = map(lambda arr1: arr1 * 2, arr1)

print(arr2)

##############################################
print()

print("Example 2 WITHOUT High order function")

birthYear = [1975,1997,2002,1995,1985]
ages = []

for i in birthYear:
    ages.append(2018-i)

print(ages)

################################################
print()

print('Example 2 WITH High Order Function')

birthYear = [1975,1997,2002,1995,1985]

ages = map(lambda birthYear: 2018-birthYear, birthYear)

print(ages)

#################################################
print()

print("Example 3 WITHOUT High order function")

persons = [
    {
        'name':'Peter',
        'age':16
    },
    {
        'name':'Mark',
        'age':18
    },
    {
        'name':'John',
        'age':27
    },
    {
        'name':'Jane',
        'age':14
    },
    {
        'name':'Tony',
        'age':24
    }
]

print(persons[int('1')].get('umur'))
fullage = []

for i in range(len(persons)):
    a = persons[i].get('umur')
    if a >= 18:
        fullage.append(persons[i])

print(fullage)