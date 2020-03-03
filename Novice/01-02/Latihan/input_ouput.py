yes_votes = 522_654
no_votes = 112_495
percentage = yes_votes / (yes_votes + no_votes)
print(percentage)

print('=============================================')

for x in range(1, 5):
    print('{0:3d} {1:4d} {2:5d}'.format(x, x*x, x*x*x))

print('=============================================')

print('12'.zfill(5))

print('=============================================')

import json
print(json.dumps([1, 'simple', 'list']))