class SeatBooking:
    def __init__(self):
        self.seats = [['F' for _ in range(6)] for _ in range(80)]
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

    def book_seat(self, row, col):
        if self.check_availability(row, col):
            self.seats[row - 1][col - 1] = 'R'
            print(f"Seat {row}{chr(64 + col)} booked successfully.")
        else:
            print(f"Seat {row}{chr(64 + col)} is not available.")

    def free_seat(self, row, col):
        if self.seats[row - 1][col - 1] == 'R':
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
                self.book_seat(row, col)
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
