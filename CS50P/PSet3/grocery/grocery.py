list = []
while True:
    try:
        a = input().strip().lower()
        list.append(a)
    except (EOFError, KeyError):
        b = sorted(set(list))
        for i in b:
            print(f"{list.count(i)} {i.upper()}")
        quit()
