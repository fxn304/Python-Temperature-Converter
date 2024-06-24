def CtoF(celsius):
    return (1.8 * celsius) + 32

def FtoC(fahrenheit):
    return (fahrenheit - 32) / 1.8

def main():
    is_running = True

    while is_running:
        print("****************************************************")
        choice = input("Select:\n 1.Celsius to Fehrenheit\n 2.Fehrenheit to Celsius\n 3.Exit\nEnter your choice: ")

        if choice == '1': 
            degreeC = float(input("Enter Celsius degree: "))
            degreeF = CtoF(degreeC)
            print(f"{degreeC:.1f} degree Celsius is {degreeF:.1f} Fahrenheit Degree")
        elif choice == '2':
            degreeF = float(input("Enter Fahrenheit degree: "))
            degreeC = FtoC(degreeF)
            print(f"{degreeF:.1f} degree Fahrenheit is {degreeC:.1f} Celsius Degree")
        elif choice == '3':
            is_running = False
        else:
            print("That is not a valid choice. Please select 1, 2, or 3.")

        print("Thank you! Have a nice day!")

main()
