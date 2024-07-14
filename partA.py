import random
import string

# Initial seat map
# Each sublist within the seats list represents a row of seats
# "X" denotes aisles, "S" denotes storage areas, and seat numbers are represented by their codes
seats = [
    ["1A", "2A", "3A", "4A", "...", "...", "77A", "78A", "79A", "80A"],
    ["1B", "2B", "3B", "4B", "...", "...", "77B", "78B", "79B", "80B"],
    ["1C", "2C", "3C", "4C", "...", "...", "77C", "78C", "79C", "80C"],
    ["X", "X", "X", "X", "...", "...", "X", "X", "X", "X"],
    ["1D", "2D", "3D", "4D", "...", "...", "S", "S", "79D", "80D"],
    ["1E", "2E", "3E", "4E", "...", "...", "S", "S", "79E", "80E"],
    ["1F", "2F", "3F", "4F", "...", "...", "S", "S", "79F", "80F"],
]

def display_seats():
    """
    Displays the current seating map.
    Each row is printed on a new line, with seat identifiers separated by spaces.
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

def book_seat(seat):
    """
    Books a given seat if it is available.
    Updates the seat to "R" to indicate it has been reserved.
    Returns True if the booking is successful, otherwise False.
    """
    for row in seats:
        if seat in row:
            if row[row.index(seat)] not in ["R", "X", "S"]:
                row[row.index(seat)] = "R"
                return True
    return False

def free_seat(seat):
    """
    Frees a previously booked seat.
    Updates the seat back to its original identifier.
    Returns True if the seat is successfully freed, otherwise False.
    """
    for row in seats:
        if seat in row:
            if row[row.index(seat)] == "R":
                row[row.index(seat)] = seat
                return True
    return False

def menu():
    """
    Displays a menu and handles user input for checking seat availability, booking, freeing a seat, displaying the seating map, and exiting the program.
    """
    while True:
        # Display the menu options
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        # Get the user's choice
        choice = input("Enter your choice: ")
        
        # Perform the chosen action
        if choice == '1':
            seat = input("Enter seat to check availability: ")
            if check_availability(seat):
                print(f"Seat {seat} is available.")
            else:
                print(f"Seat {seat} is not available.")
        elif choice == '2':
            seat = input("Enter seat to book: ")
            if book_seat(seat):
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

# Run the menu function if this module is the main program
if __name__ == "__main__":
    menu()
