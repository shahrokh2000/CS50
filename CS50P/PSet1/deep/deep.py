a = ['42', 'forty-two', 'forty two']
b = input('What is the Answer to the Great Question of Life, the Universe, and Everything?').strip().lower()
if b in a:
    print('Yes')
else:
    print('NO')
