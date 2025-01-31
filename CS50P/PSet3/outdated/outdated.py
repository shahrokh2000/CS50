months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        a = input("Date: ").strip()

        if " " in a:
            if "," in a:
                month, day, year = a.split(" ")
                if month.title() in months:
                    month = int(months.index(month)+1)
                    day = int(day.strip(","))
                    if month <= 12 and day <= 31:
                        print(f"{year}-{month:02}-{day:02}")
                        break

        else:
            month,  day, year = map(int, a.split("/"))
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
    except ValueError:
        continue

    except (EOFError, KeyboardInterrupt):
        print()
        quit()
