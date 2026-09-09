from datetime import datetime

print("\n" + "=" * 50)
print("                    HOTEL")
print("=" * 50)


while True:
	name = input("\n Enter your name: ").strip()
	
	if name.isalpha():
		print(name)
		break
	else:
		print("Invalid name")
		
		
while True:
    age = input("\nEnter your age: ")

    if age.isdigit():
        age = int(age)
        print(age)
        break
    else:
        print("Invalid age")

		
while True:
	address = input("\nEnter your address: ").strip()
	
	if address.isalpha():
	   print(address)
	   break
	else:
		print("Invalid address")
	

while True:
	nationality = input("\nEnter your nationality: ").strip()
	
	if nationality.isalpha():
		print(nationality)
		break
		
	else:
		print('invalid nationality')
		
	

rooms = {
    "room101": 550,
    "room102": 500,
    "room103": 300,
    "room104": 350,
    "room105": 750
}

print("\nAvailable Rooms:")

for room, price in rooms.items():
    print(f"{room} - ${price} per day")
choice = input("\nChoose your room: ").strip().lower()
if choice not in rooms:
    print("\nSorry, this room is not available.")
else:
    print("\nRoom is available!")
    booking_type = input("Do you want to book by days or hours? ").strip().lower()
    if booking_type == "days":
        days = int(input("Enter number of days: "))
        total = days * rooms[choice]
    elif booking_type == "hours":
        hours = int(input("Enter number of hours: "))
        total = hours * (rooms[choice] / 24)
    else:
        print("Invalid booking type.")
        exit()


print("\n" + "=" * 50)
print("                    RESTAURANT")
print("=" * 50)
breakfast = {
    "pie": 20,
    "cheese": 15,
    "beans": 10
}

lunch = {
    "pizza": 200,
    "pasta": 150,
    "burger": 100
}

restaurant = input("Do you want breakfast or lunch? (yes/no): ").strip().lower()

if restaurant == "yes":
    meal = input("Do you want breakfast or lunch? ").strip().lower()

    if meal == "breakfast":
        print("\nAvailable breakfast:")

        for food, price in breakfast.items():
            print(f"{food} - ${price} per day")

        choice_meal = input("\nChoose your breakfast: ").strip().lower()

        if choice_meal in breakfast:
            total2 = total + breakfast[choice_meal]
            
        else:
            print("Invalid breakfast choice")

    elif meal == "lunch":
        print("\nAvailable lunch:")

        for food, price in lunch.items():
            print(f"{food} - ${price} per day")

        choice_meal = input("\nChoose your lunch: ").strip().lower()

        if choice_meal in lunch:
            total2 = total + lunch[choice_meal]
        
        else:
            print("Invalid lunch choice")

    else:
        print("Invalid meal choice")

elif restaurant == "no":
    print("Okay")
    total2 = total

else:
    print("No answer")

    
    now = datetime.now()
    print("\n" + "=" * 50)
    print("                CUSTOMER INFORMATION")
    print("=" * 50)
    print(f"Name        : {name}")
    print(f"Age         : {age}")
    print(f"Address     : {address}")
    print(f"Nationality : {nationality}")
    print(f"Room        : {choice}")
    print(f"Booking     : {booking_type}")
    print(f"Total       : ${total2:.2f}")
    print(f"Date        : {now.date()}")
    print(f"Time        : {now.strftime('%H:%M:%S')}")

    print("=" * 50)
    print("          Thank you for choosing our hotel")
    print("=" * 50)
