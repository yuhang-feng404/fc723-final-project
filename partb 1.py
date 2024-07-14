import random
import string

# Set to store existing booking references to ensure uniqueness
existing_references = set()

def generate_unique_reference():
    """
    Generates a unique 8-character alphanumeric booking reference.
    
    The function generates a random string of 8 alphanumeric characters and checks if it
    already exists in the existing_references set. If the reference is unique, it adds it
    to the set and returns it. Otherwise, it continues generating until a unique reference
    is found.
    
    Returns:
        str: A unique 8-character alphanumeric booking reference.
    """
    while True:
        # Generate a random 8-character alphanumeric string
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        
        # Check if the generated reference is unique
        if reference not in existing_references:
            # If unique, add the reference to the set
            existing_references.add(reference)
            return reference

# Example usage
print(generate_unique_reference())
