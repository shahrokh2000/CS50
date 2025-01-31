x, y, z, = input('Expression: ').strip().split(' ')
x = float(x)
z = float(z)

if y == '+':
    ans = x + z

elif y == '-':
    ans = x - z

elif y == '*':
    ans = x * z

elif y == '/':
    ans = x / z

print(f"{ans:.1f}")
