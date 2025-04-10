import re
from art import *
tprint("PASSWORD     CHECKER")
def strength_check(password):
    criteria = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digits': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }

    score = sum(criteria.values())

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = "Password Strength: " + strength + "\n"
    if not criteria['length']:
        feedback += "- Should be at least 8 characters long\n"
    if not criteria['uppercase']:
        feedback += "- Add at least one uppercase letter\n"
    if not criteria['lowercase']:
        feedback += "- Add at least one lowercase letter\n"
    if not criteria['digits']:
        feedback += "- Include at least one number\n"
    if not criteria['special']:
        feedback += "- Include at least one special character (e.g., !, @, #, etc.)\n"

    return feedback

if __name__ == "__main__":
    password = input("Enter your password: ")
    print(strength_check(password))
