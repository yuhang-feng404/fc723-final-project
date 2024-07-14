import random
import string

# Initial seat map with placeholders for missing seats
seats = [
    ["1A", "2A", "3A", "4A", "...", "...", "77A", "78A", "79A", "80A"],
    ["1B", "2B", "3B", "4B", "...", "...", "77B", "78B", "79B", "80B"],
    ["1C", "2C", "3C", "4C", "...", "...", "77C", "78C", "79C", "80C"],
    ["X", "X", "X", "X", "...", "...", "X", "X", "X", "X"],
    ["1D", "2D", "3D", "4D", "...", "...", "S", "S", "79D", "80D"],
    ["1E", "2E", "3E", "4E", "...", "...", "S", "S", "79E", "80E"],
    ["1F", "2F", "3F", "4F", "...", "...", "S", "S", "79F", "80F"],
]

# Dictionary to store booking references and customer details
booking_data = {}

def display_seats():
    """
    Displays the current state of the seats.
    """
    for row in seats:
        print(" ".join(row))

def check_availability(seat):
    """
    Checks if a specific seat is available.
    
    Args:
    seat (str): The seat identifier.
    
    Returns:
    bool: True if the seat is available, False otherwise.
    """
    for row in seats:
        if seat in row:
            # Seat is available if it is not marked as "R" (reserved), "X" (blocked), or "S" (special)
            return True if row[row.index(seat)] not in ["R", "X", "S"] else False
    return False

def generate_booking_reference():
    """
    Generates a unique 8-character alphanumeric booking reference.
    
    Returns:
    str: A unique booking reference.
    """
    while True:
        # Generate a random 8-character alphanumeric string
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Ensure the reference is unique
        if reference not in booking_data:
            return reference

def book_seat(seat, passport, first_name, last_name):
    """
    Books a seat and stores customer details.
    
    Args:
    seat (str): The seat identifier.
    passport (str): Customer's passport number.
    first_name (str): Customer's first name.
    last_name (str): Customer's last name.
    
    Returns:
    bool: True if the seat is successfully booked, False otherwise.
    """
    for row in seats:
        if seat in row:
            if row[row.index(seat)] not in ["R", "X", "S"]:
                # Generate a booking reference
                booking_reference = generate_booking_reference()
                # Mark the seat as reserved with the booking reference
                row[row.index(seat)] = booking_reference
                # Store the customer details associated with the booking reference
                booking_data[booking_reference] = {
                    "passport": passport,
                    "first_name": first_name,
                    "last_name": last_name,
                    "seat": seat
                }
                return True
    return False

def free_seat(seat):
    """
    Frees a booked seat and removes customer details.
    
    Args:
    seat (str): The seat identifier.
    
    Returns:
    bool: True if the seat is successfully freed, False otherwise.
    """
    for row in seats:
        if seat in row:
            booking_reference = row[row.index(seat)]
            if booking_reference not in ["F", "X", "S"]:
                # Reset the seat to its original identifier
                row[row.index(seat)] = seat
                # Remove the customer details associated with the booking reference
                if booking_reference in booking_data:
                    del booking_data[booking_reference]
                return True
    return False

def menu():
    """
    Displays the menu and processes user input.
    """
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        # Get user choice and validate input
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
