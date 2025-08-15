def get_input():
    while True:
        g = input("Grade (1.0 - 5.0) or 'done': ").strip().lower()
        if g == "done":
            return None, None
        try:
            g = float(g)
        except:
            print("Not a number. Try again.")
            continue
        if g < 1.0 or g > 5.0:
            print("Grade must be between 1.0 and 5.0.")
            continue

        try:
            u = float(input("Units: "))
        except:
            print("Not a number for units.")
            continue
        if u <= 0:
            print("Units must be more than 0.")
            continue
        return g, u

def calc_gwa(data):
    total_units = 0
    total_points = 0
    for grade, unit in data:
        total_points += grade * unit
        total_units += unit
    if total_units == 0:
        return 0
    return total_points / total_units

def honors(gwa):
    if gwa <= 1.50:
        return "Director's Lister"
    elif gwa <= 3.00:
        return "You passed"
    else:
        return "You failed"

print("=== General Weighted Average Calculator ===")
while True:
    data = []
    while True:
        grade, units = get_input()
        if grade is None:
            break
        data.append((grade, units))

    if len(data) == 0:
        print("No grades entered!")
        continue

    gwa = calc_gwa(data)
    print("\nYour GWA:", round(gwa, 2))
    print("Honor Status:", honors(gwa))

    again = input("\nAnother calculation? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for using this program!")
        break