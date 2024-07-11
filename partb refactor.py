import random
import string

class SeatBooking:
    def __init__(self):
        # Initialize seats and bookings
        self.seats = [['F' for _ in range(6)] for _ in range(80)]  # 80 rows of seats with 6 columns each
        self.bookings = {}  # Dictionary to store booking details
        self.existing_references = set()  # Set to store unique booking references
        self.initialize_seats()  # Initialize seat layout with aisles and storage areas

    def initialize_seats(self):
        # Set aisles ('X') and storage areas ('S') in the seat layout
        for i in range(80):
            self.seats[i][3] = 'X'  # Aisle
            self.seats[i][5] = 'X'  # Aisle
        for i in range(77, 80):
            self.seats[i][4] = 'S'  # Storage

    def display_seats(self):
        # Print the current seat layout
        for row in self.seats:
            print(' '.join(row))

    def check_availability(self, row, col):
        # Check if a specific seat is free
        return self.seats[row - 1][col - 1] == 'F'

    def generate_booking_reference(self):
        # Generate a unique 8-character alphanumeric booking reference
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.existing_references:
                self.existing_references.add(reference)
                return reference

    def book_seat(self, row, col, passport_number, first_name, last_name):
        # Book a seat if it's available, and store booking details
        if self.check_availability(row, col):
            reference = self.generate_booking_reference()  # Generate a unique booking reference
            self.seats[row - 1][col - 1] = reference  # Mark the seat with the booking reference
            # Store booking details in the bookings dictionary
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
        # Free a booked seat and remove booking details
        reference = self.seats[row - 1][col - 1]  # Get the booking reference for the seat
        if reference in self.bookings:
            del self.bookings[reference]  # Remove booking details from the dictionary
            self.existing_references.remove(reference)  # Remove the reference from the set of existing references
            self.seats[row - 1][col - 1] = 'F'  # Mark the seat as free
            print(f"Seat {row}{chr(64 + col)} freed successfully.")
        else:
            print(f"Seat {row}{chr(64 + col)} is not booked.")

    def show_booking_state(self):
        # Display the current booking state of all seats
        self.display_seats()

    def menu(self):
        # Display the menu and handle user input
        while True:
            print("\nMenu:")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking state")
            print("5. Exit program")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                # Handle seat availability check
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                if self.check_availability(row, col):
                    print(f"Seat {row}{chr(64 + col)} is available.")
                else:
                    print(f"Seat {row}{chr(64 + col)} is not available.")
            elif choice == '2':
                # Handle seat booking
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                passport_number = input("Enter passport number: ")
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                self.book_seat(row, col, passport_number, first_name, last_name)
            elif choice == '3':
                # Handle seat freeing
                row = int(input("Enter row number: "))
                col = int(input("Enter column number: "))
                self.free_seat(row, col)
            elif choice == '4':
                # Handle displaying booking state
                self.show_booking_state()
            elif choice == '5':
                # Exit the program
                print("Exiting program.")
                break
            else:
                # Handle invalid menu choice
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    sb = SeatBooking()
    sb.menu()
