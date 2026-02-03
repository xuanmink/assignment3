while True:
    try:
        inches = float(input("Enter length in inches (no negative num): "))
        if inches < 0:
            print("Program ended.")
            break
        cm = inches * 2.54
        print(f"{inches} inches = {cm:.2f} centimeters")
    except ValueError:
        print("Please enter a valid number")