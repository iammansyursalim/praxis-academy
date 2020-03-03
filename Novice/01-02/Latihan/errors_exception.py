
#while True:
#    try:
#        x = int(input("Please enter a number: "))
#        break
#    except ValueError:
#        print("Oops!  That was no valid number.  Try again..."

#######################################   

#try:
#    raise NameError('HiThere')
#except NameError:
#    print('An exception flew by!')
#    raise

 ########################

def bool_return():
    try:
        return True
    finally:
        return False

print(bool_return())