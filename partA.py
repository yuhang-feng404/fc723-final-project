class SeatBooking:
    def __init__(self, rows=80, columns=['A', 'B', 'C', 'D', 'E', 'F']):
        """
        Initialize the SeatBooking class with a default layout.
        """
        self.rows = rows
        self.columns = columns
        self.seats = self.create_seat_layout()

    def create_seat_layout(self):
        """
        Create the initial layout of the seats. 'F' for free, 'X' for aisle, and 'S' for storage.
        """
        layout = {}
        for column in self.columns:
            layout[column] = ['F' for _ in range(self.rows)]
        return layout

    def display_seats(self):
        """
        Display the current booking state of the seats.
        """
        for column in self.columns:
            print(f"{column}: ", end="")
            for seat in self.seats[column]:
                print(seat, end=" ")
            print()

    def check_availability(self, row, column):
        """
        Check if a specific seat is available.
        """
        if self.seats[column][row-1] == 'F':
            return True
        return False

    def book_seat(self, row, column):
        """
        Book a specific seat if it is available.
        """
        if self.check_availability(row, column):
            self.seats[column][row-1] = 'R'
            print(f"Seat {row}{column} has been booked.")
        else:
            print(f"Seat {row}{column} is already booked or unavailable.")

    def free_seat(self, row, column):
        """
        Free a booked seat.
        """
        if self.seats[column][row-1] == 'R':
            self.seats[column][row-1] = 'F'
            print(f"Seat {row}{column} has been freed.")
        else:
            print(f"Seat {row}{column} is not booked.")

    def menu(self):
        """
        Display a menu for the user to interact with the seat booking system.
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
            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            # Execute the chosen menu option
            if choice == 1:
                # Check availability of a seat
                try:
                    row = int(input("Enter seat row number: "))
                    column = input("Enter seat column letter: ").upper()
                    if column not in self.columns:
                        print("Invalid column letter.")
                        continue
                    if not (1 <= row <= self.rows):
                        print("Invalid row number.")
                        continue
                    if self.check_availability(row, column):
                        print(f"Seat {row}{column} is available.")
                    else:
                        print(f"Seat {row}{column} is not available.")
                except ValueError:
                    print("Invalid input. Please enter valid row number.")
            elif choice == 2:
                # Book a seat
                try:
                    row = int(input("Enter seat row number: "))
                    column = input("Enter seat column letter: ").upper()
                    if column not in self.columns:
                        print("Invalid column letter.")
                        continue
                    if not (1 <= row <= self.rows):
                        print("Invalid row number.")
                        continue
                    self.book_seat(row, column)
                except ValueError:
                    print("Invalid input. Please enter valid row number.")
            elif choice == 3:
                # Free a booked seat
                try:
                    row = int(input("Enter seat row number: "))
                    column = input("Enter seat column letter: ").upper()
                    if column not in self.columns:
                        print("Invalid column letter.")
                        continue
                    if not (1 <= row <= self.rows):
                        print("Invalid row number.")
                        continue
                    self.free_seat(row, column)
                except ValueError:
                    print("Invalid input. Please enter valid row number.")
            elif choice == 4:
                # Show booking state
                self.display_seats()
            elif choice == 5:
                # Exit the program
                print("Exiting program.")
                break
            else:
                # Invalid menu choice
                print("Invalid choice. Please try again.")

# Example usage
seat_booking = SeatBooking()
seat_booking.menu()
