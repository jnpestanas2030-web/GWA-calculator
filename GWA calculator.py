def percent_to_grade(p):
    """Convert percentage to grade equivalent."""
    if p >= 95: return 1.0
    elif p >= 90: return 1.25
    elif p >= 85: return 1.5
    elif p >= 80: return 1.75
    elif p >= 75: return 2.0
    elif p >= 70: return 2.25
    elif p >= 65: return 2.5
    elif p >= 60: return 2.75
    elif p >= 55: return 3.0
    elif p >= 50: return 4.0
    else: return 5.0


#To get the user input for grade and units
def get_input(mode):
    while True:
        grade_input = input("Enter subject grade (or 'done' to finish): ").strip().lower()
        if grade_input == "done":
            return None, None

        try:
            grade_input = float(grade_input)
        except:
            print("Not a number. Try again.")
            continue

        # If using percentage grading
        if mode == "percent":
            if grade_input < 0 or grade_input > 100:
                print("Percentage must be between 0 and 100.")
                continue
            grade_input = percent_to_grade(grade_input)
            print(f"Converted to GWA grade: {grade_input}")

        # If using direct GWA grading
        else:
            if grade_input < 1.0 or grade_input > 5.0:
                print("GWA must be between 1.0 and 5.0.")
                continue

        try:
            units = float(input("Enter subject units: "))
        except:
            print("Units must be a number.")
            continue

        if units <= 0:
            print("Units must be greater than 0.")
            continue

        return grade_input, units

#GWA calculation
def calc_gwa(data):
    total_units = sum(units for _, units in data)
    if total_units == 0:
        return 0
    total_points = sum(grade * units for grade, units in data)
    return total_points / total_units


print("=== GWA Calculator ===")

while True:
    #Ask user what type of grade input (Percentage or Gwa) is the user gonna enter
    print("\nChoose what grade input type(1 or 2):")
    print("1 - Percentage")
    print("2 - GWA (1.0–5.0)")
    mode = input("> ").strip()

    if mode == "1":
        mode = "percent"
    elif mode == "2":
        mode = "gwa"
    else:
        print("Invalid choice. Try again.")
        continue

    data = []

    while True:
        grade_input, units = get_input(mode)
        if grade_input is None:
            break
        data.append((grade_input, units))

    if not data:
        print("No grades entered!")
        continue

    #To output the grade and to output if in what category is the user 
    gwa = calc_gwa(data)
    print("\nYour General Weighted Average (GWA) is:", round(gwa, 2))
    if gwa <= 1.50:
        print("Classification: Director's Lister")
    elif gwa <= 3.00:
        print("Classification: You passed")
    else:
        print("Classification: You failed") 
    
    #Ask if the user wants to calculate again
    again = input("\nAnother calculation? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for using the program!")
        break
