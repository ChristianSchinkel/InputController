"""Input Controller Module."""

class InputController:
    """Class to handle input control."""

    def __init__(self):
        """Initialize the Input Controller."""
        pass

    def check_input_is_string(self, user_input: str) -> bool:
        """Check if the input is a string."""
        return isinstance(user_input, str)

    def format_int(self, prompt: str, user_input: str) -> int:
        """Format the input as an integer. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :param user_input: The input from the user.
        :return: The formatted integer.
        """
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def format_float(self, prompt: str, user_input: str) -> float:
        """Format the input as a float. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :param user_input: The input from the user.
        :return: The formatted float.
        """
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a float.")

    def format_bool(self, prompt: str, user_input: str) -> bool:
        """Format the input as a boolean. If it fails,
        raises a ValueError. And ask the user to input again.
        :param prompt: The prompt to display to the user.
        :param user_input: The input from the user.
        :return: The formatted boolean.
        """
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'y', 'true', 't']:
                return True
            elif response in ['no', 'n', 'false', 'f']:
                return False
            else:
                print("Invalid input. Please enter yes or no.")

    def contain_float_separator(self, user_input: str) -> bool:
        """Check if the input has a '.' or a ',' to determine if it's a float."""
        return '.' in user_input or ',' in user_input

    def is_integer(self, user_input: str) -> bool:
        """Check if the input string contains a float separator.
        and if it does, return False.
        If the input contains string characters
        other than numbers, return False.
        """
        # If the input has a float separator, it's not an integer.
        has_float_separator = self.contain_float_separator(user_input)
        # If the input contains only digits, it's an integer.
        is_digit = user_input.isdigit()

        # Return True only if it's all digits and has no float separator.
        return is_digit and not has_float_separator

    def replace_float_separator(self, user_input: str) -> str:
        """Replace ',' with '.' in the input string."""
        return user_input.replace(',', '.')


def main():
    """Main function for Input Controller."""
    controller = InputController()
    print("This is the Input Controller Module.")
    # Example usage
    user_string = controller.check_input_is_string("Hello")
    print(f"Is 'Hello' a string? {user_string}")
    user_int = controller.format_int("Enter an integer: ", "")
    print(f"You entered integer: {user_int}")
    user_float = controller.format_float("Enter a float: ", "")
    print(f"You entered float: {user_float}")
    user_bool = controller.format_bool("Enter yes or no: ", "")
    print(f"You entered boolean: {user_bool}")


if __name__ == "__main__":
    main()