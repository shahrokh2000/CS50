while True:
    tank = input("Fraction: ").strip()
    try:
        u, d = tank.split("/")
        if u.isdigit() and d.isdigit():
            if int(u) <= int(d) and int(d) != 0:
                fuel = (int(u) / int(d)) * 100
                if fuel >= 99:
                    print("F")
                    break
                elif fuel < 99 and fuel > 1:
                    print(f"{fuel:.0f}%")
                    break
                else:
                    print("E")
                    break
    except (ValueError, ZeroDivisionError):
        pass
    else:
        pass
