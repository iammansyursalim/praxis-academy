print(list(map(int,['1','2','3'])))

print()

def hello_world(h):
    def world(w):
        print(h,w)
    return world #mengembalikan fungsi 

h = hello_world #assigning
x = h('hello') #assigning
print(x)

x('world')
print(x)

print()

function_list = [h,x]
print(function_list)