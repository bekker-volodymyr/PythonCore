print(5 == 5)
print(5 > 6)
print( 5 == 5 and 6 > 10)

number = int(input("Enter number: "))

if number > 10:
    print(f"{number} bigger then 10")
elif number < 10:
    print(f"{number} less then 10")
else:
    print(f"{number} equals 10")

isBigger = "Yes" if number > 10 else "No"

age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)

print(isBigger)

month = input("Enter month: ")

match month:
    case "Jan" | "Fab" | "Dec":
        print("Winter")
    case _: 
        print("Not winter")