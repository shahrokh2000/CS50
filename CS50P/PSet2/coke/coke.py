cost = 50
gain = 0

while gain < cost:
    print(f"Amount Due: {cost - gain}")
    a = int(input("Insert Coin: "))
    if a == 5 or a == 10 or a == 25:
        gain += a
    else:
        continue

print(f"Change Owed: {gain - cost}")
