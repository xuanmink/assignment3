numbers = []
while True:
    user_input= input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        num= float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number")
if numbers:
    print(f"Smallest number:{min(numbers)}")
    print(f"Largest number: {max(numbers)}")
else:
    print("No numbers were entered")