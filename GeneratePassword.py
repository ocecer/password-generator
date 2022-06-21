import string
import random


class generatePassword:
    # Define variables.
    chars = []
    generatedPassword_lst = []
    generatedPassword_str = ""

    # Get the parameters from user.
    def __init__(self, _passLength=16, _isUppercase=True, _isLowercase=True, _isNumber=True, _isSymbol=True):
        self.passLength = _passLength
        self.uppercase = _isUppercase
        self.lowercase = _isUppercase
        self.number = _isNumber
        self.symbol = _isSymbol

    def gp(self):
        # Create chars list.
        if self.uppercase:
            self.chars.extend(list(string.ascii_uppercase))
        if self.lowercase:
            self.chars.extend(list(string.ascii_lowercase))
        if self.number:
            self.chars.extend(list(string.digits))
        if self.symbol:
            self.chars.extend(list("!@#$%^&*()-_=+-?<>.,"))

        # Shuffle the char list.
        random.shuffle(self.chars)

        # Pick random characters from chars and write into generatedPassword_lst.
        for i in range(self.passLength):
            self.generatedPassword_lst.append(random.choice(self.chars))

        # Shuffle the generatedPassword_lst.
        generatedPassword_lst = random.shuffle(self.generatedPassword_lst)

        # Convert generatedPassword_lst into string.
        self.generatedPassword_str = self.generatedPassword_str.join(
            self.generatedPassword_lst)

        # Return the generated password.
        return f"\nGenerated Password: {self.generatedPassword_str}\n"
