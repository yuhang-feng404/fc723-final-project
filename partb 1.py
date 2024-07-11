import random
import string

class BookingSystem:
    def __init__(self):
        self.existing_references = set()

    def generate_booking_reference(self):
        while True:
            reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            if reference not in self.existing_references:
                self.existing_references.add(reference)
                return reference
