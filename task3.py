import string
import random


class PasswordGenerator:
    def __init__(self, length, use_lower, use_upper, use_number, use_special):
        self.length = length
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_number = use_number
        self.use_special = use_special

    def generate_password(self):
        # Define character sets
        lower_chars = list(string.ascii_lowercase)
        upper_chars = list(string.ascii_uppercase)
        number_chars = list(string.digits)
        special_chars = ['$', '%', '^', '&', '*',
                         '(', ')', '_', '+', '=', '-', '!', ';', ':', ',', '.', '[', ']', '{', '}']

        # Initialize the list of allowed character sets and password
        allowed_sets = []
        password = ""

        # Check and add lower case characters
        if self.use_lower:
            allowed_sets.append(lower_chars)
            password += random.choice(lower_chars)

        # Check and add upper case characters
        if self.use_upper:
            allowed_sets.append(upper_chars)
            password += random.choice(upper_chars)

        # Check and add numbers
        if self.use_number:
            allowed_sets.append(number_chars)
            password += random.choice(number_chars)

        # Check and add special characters
        if self.use_special:
            allowed_sets.append(special_chars)
            password += random.choice(special_chars)

        # Validate that at least one set is allowed
        if not allowed_sets:
            print("At least one character set must be allowed.")
            return None

        # Generate the remaining characters randomly
        for _ in range(self.length - len(password)):
            selected_set = random.choice(allowed_sets)
            password += random.choice(selected_set)

        # Shuffle the password characters for randomness
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)

        return password


if __name__ == "__main__":
    print("Password Generator")
    password_length = int(input("Length: "))
    include_lower = input("Lowercase (y/n): ").lower() == 'y'
    include_upper = input("Uppercase (y/n): ").lower() == 'y'
    include_number = input("Numbers (y/n): ").lower() == 'y'
    include_special = input(
        "Special Characters (y/n): ").lower() == 'y'

    password_generator = PasswordGenerator(
        password_length, include_lower, include_upper, include_number, include_special)
    generated_password = password_generator.generate_password()

    if generated_password:
        print("Your Password is", generated_password)
