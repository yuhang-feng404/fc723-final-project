class SeatBooking:
    def __init__(self):
        self.seats = [['F' for _ in range(6)] for _ in range(80)]
        self.bookings = {}
        self.existing_references = set()
        self.initialize_seats()

    def initialize_seats(self):
        # Initialize aisles ('X') and storage ('S')
        for i in range(80):
            self.seats[i][3] = 'X'  # Aisle
            self.seats[i][5] = 'X'  # Aisle
        for i in range(77, 80):
            self.seats[i][4] = 'S'  # Storage

    def display_seats(self):
        for row in self.seats:
            print(' '.join(row))

    def check_availability(self, row, col):
        return self.seats[row - 1][col - 1] == 'F'

    def generate_booking_reference(self):
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.existing_references:
                self.existing_references.add(reference)
                return reference

    def book_seat(self, row, col, passport_number, first_name, last_name):
        if self.check_availability(row, col):
            reference = self.generate_booking_reference()
            self.seats[row - 1][col - 1] = reference
            self.bookings[reference] = {
                'passport_number': passport_number,
                'first_name': first_name,
                'last_name': last_name,
                'seat': f"{row}{chr(64 + col)}"
            }
            print(f"Seat {row}{chr(64 + col)} booked successfully with reference {reference}.")
        else:
            print(f"Seat {row}{chr(64 + col)} is not available.")

    def free_seat(self, row, col):
        reference = self.seats[row - 1][col - 1]
        if reference in self.bookings:
            del self.bookings[reference]
            self.existing_references.remove(reference)
            self.seats[row - 1][col - 1] = 'F'
            print(f"Seat {row}{chr(64 + col)} freed successfully.")
        else:
            print(f"Seat {row}{chr(64 + col)} is not booked.")

    def show_booking_state(self):
        self.display_seats()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = input("Enter your choice: ")

            if choice == '1':
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                if self.check_availability(row, col):
                    print(f"Seat {row}{chr(64 + col)} is available.")
                else:
                    print(f"Seat {row}{chr(64 + col)} is not available.")
            elif choice == '2':
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                passport_number = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                self.book_seat(row, col, passport_number, first_name, last_name)
            elif choice == '3':
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                self.free_seat(row, col)
            elif choice == '4':
                self.show_booking_state()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    sb = SeatBooking()
    sb.menu()

