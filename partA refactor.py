import random
import string

# Initial seat map
# Each list within the seats list represents a row of seats
# "X" denotes aisles, "S" denotes storage areas, and actual seat numbers are represented by their codes
seats = [
    ["1A", "2A", "3A", "4A", "...", "...", "77A", "78A", "79A", "80A"],
    ["1B", "2B", "3B", "4B", "...", "...", "77B", "78B", "79B", "80B"],
    ["1C", "2C", "3C", "4C", "...", "...", "77C", "78C", "79C", "80C"],
    ["X", "X", "X", "X", "...", "...", "X", "X", "X", "X"],
    ["1D", "2D", "3D", "4D", "...", "...", "S", "S", "79D", "80D"],
    ["1E", "2E", "3E", "4E", "...", "...", "S", "S", "79E", "80E"],
    ["1F", "2F", "3F", "4F", "...", "...", "S", "S", "79F", "80F"],
]

# Dictionary to store booking information
# The key is the unique booking reference, and the value is a dictionary of customer details
booking_data = {}

# Set to store existing booking references to ensure uniqueness
existing_references = set()

def generate_unique_reference():
    """
    Generates a unique 8-character alphanumeric booking reference.
    Ensures the reference is unique by checking against existing_references.
    """
    while True:
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if reference not in existing_references:
            existing_references.add(reference)
            return reference

def display_seats():
    """
    Displays the current seating map.
    """
    for row in seats:
        print(" ".join(row))

def check_availability(seat):
    """
    Checks if a given seat is available for booking.
    Returns True if the seat is available (i.e., not "R", "X", or "S"), otherwise False.
    """
    for row in seats:
        if seat in row:
            return True if row[row.index(seat)] not in ["R", "X", "S"] else False
    return False

def book_seat(seat, passport, first_name, last_name):
    """
    Books a seat for a customer.
    Updates the seat to store a unique booking reference and saves customer details in booking_data.
    Returns True if booking is successful, otherwise False.
    """
    for row in seats:
        if seat in row:
            if row[row.index(seat)] not in ["R", "X", "S"]:
                reference = generate_unique_reference()
                row[row.index(seat)] = reference
                booking_data[reference] = {
                    "passport": passport,
                    "first_name": first_name,
                    "last_name": last_name,
                    "seat": seat
                }
                return True
    return False

def free_seat(seat):
    """
    Frees a previously booked seat.
    Updates the seat status to "F" and removes the booking details from booking_data.
    Returns True if the seat is successfully freed, otherwise False.
    """
    for row in seats:
        if seat in row:
            reference = row[row.index(seat)]
            if reference in booking_data:
                row[row.index(seat)] = "F"
                del booking_data[reference]
                return True
    return False

def menu():
    """
    Displays a menu and handles user input for checking seat availability, booking, freeing a seat, displaying the seating map, and exiting the program.
    """
    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            seat = input("Enter seat to check availability: ")
            if check_availability(seat):
                print(f"Seat {seat} is available.")
            else:
                print(f"Seat {seat} is not available.")
        elif choice == '2':
            seat = input("Enter seat to book: ")
            passport = input("Enter passport number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            if book_seat(seat, passport, first_name, last_name):
                print(f"Seat {seat} has been booked.")
            else:
                print(f"Seat {seat} cannot be booked.")
        elif choice == '3':
            seat = input("Enter seat to free: ")
            if free_seat(seat):
                print(f"Seat {seat} has been freed.")
            else:
                print(f"Seat {seat} cannot be freed.")
        elif choice == '4':
            display_seats()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

# Run the menu
if __name__ == "__main__":
    menu()
