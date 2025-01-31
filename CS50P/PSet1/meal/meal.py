def main():
    sch = [
        {"meal": "breakfast time", "start hour": 7, "end hour": 8},
        {"meal": "lunch time", "start hour": 12, "end hour": 13},
        {"meal": "dinner time", "start hour": 18, "end hour": 19},
    ]

    time = float(convert(input("what time is it? ")))

    for d in sch:
        if time >= float(d["start hour"]) and time <= float(d["end hour"]):
            print(d["meal"])


def convert(time):
    c = 0.0
    if time.rfind(" a.m.") != -1:
        time = time.repalce(" a.m.", "")
    elif time.rfind(" p.m.") != -1:
        time = time.repalce(" p.m.", "")
        c = 12.0
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60) + c
    return t


if __name__ == "__main__":
    main()
