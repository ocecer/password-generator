import GeneratePassword as gp
import easyQuestion as eq

initialString = """
    \n**********
    This program is desiged to create randomly generated passwords according to user\'s desired characters.
    The program supports following characters for password. CTRL+C to terminate the program.

    - Uppercase and lowercase alphabetich characters (A/a...z/Z).
    - Numeric characters (1...9).
    - Special charcters (!@#$%^&*()-_=+-?<>.,).
    - Custom characters.
    **********\n
"""

print(initialString)
# Set min and max legth of the password.
minPassLength = 4
maxPassLength = 50

i = 0
while i < 3:

    try:
        # Define pass length.
        passLength = int(eq.easyQuestoin(
            "num", "Password length (4-50)", minPassLength, maxPassLength))
    except TypeError:
        break

    # Get the password char preference of the user.
    uppercasePreference = eq.easyQuestoin(
        "yn", "Include uppercase characters (y/n)")
    lowercasePreference = eq.easyQuestoin(
        "yn", "Include lowercase characters (y/n)")
    numberPreference = eq.easyQuestoin("yn", "Include numbers (y/n)")
    symbolPreference = eq.easyQuestoin(
        "yn", "Include symbols (!@#$%^&*()-_=+-?<>.,) (y/n)")

    # If none of the preferences selected ask user again. Max 3 times.
    if uppercasePreference or lowercasePreference or numberPreference or symbolPreference:
        # Generated password.
        generatedPassword = gp.generatePassword(
            passLength, uppercasePreference, lowercasePreference, numberPreference, symbolPreference).gp()
        # Print generated password.
        print(generatedPassword)
        break
    else:

        if i < 2:
            i += 1
            print(
                f"\nAt least one character set should be seleted. {3-i}/3 try left.\n")
        else:
            print("\n0 try left. Program is terminated.\n")
            break
