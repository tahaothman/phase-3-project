import sys

from reservation_system import (
    check_in_customer,
    check_out_customer,
    list_available_rooms,
    list_reservations,
)


def main():
    while True:
        print("1. Check-In")
        print("2. Check-Out")
        print("3. Show Available Rooms")
        print("4. List Reservations")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            check_in_customer()
        elif choice == '2':
            check_out_customer()
        elif choice == '3':
            list_available_rooms()
        elif choice == '4':
            list_reservations()
        elif choice == '5':
            sys.exit(0)

if __name__ == "__main__":
    main()
