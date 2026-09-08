from datetime import datetime

print("\n" + "=" * 50)
print("                    HOTEL")
print("=" * 50)

name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
address = input("Enter your address: ").strip()
nationality = input("Enter your nationality: ").strip()

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
    print(f"Total       : ${total:.2f}")
    print(f"Date        : {now.date()}")
    print(f"Time        : {now.strftime('%H:%M:%S')}")

    print("=" * 50)
    print("          Thank you for choosing our hotel")
    print("=" * 50)
