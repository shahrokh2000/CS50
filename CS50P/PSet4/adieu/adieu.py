import inflect

p = inflect.engine()
names = []

while True:
    try:
        a = str(input("Name: ")).strip()
        names.append(a)
    except(EOFError, KeyError):
        print(f"Adieu, adieu, to {p.join(names)}", end="\n")
        quit()
