names = ['Shivani', 'Jan', 'Yusef', 'Sakura']
# Instead of: map(lambda x: 'Hi ' + x, names), we can do
greeted_names = ['Hi ' + name for name in names]

print(greeted_names)