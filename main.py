import random
import string
import re
import math

# Function to generate a more advanced, customizable password
def generate_password(length=20, include_upper=True, include_lower=True, include_digits=True, include_special=True, exclude_ambiguous=True):
    if length < 16:
        print("Warning: Password length is less than recommended (16). Using 16 as minimum.")
        length = 16  # Ensuring minimum password length is 16

    # Base character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation

    # Exclude ambiguous characters like '0', 'O', 'l', 'I'
    ambiguous_chars = "0OIl"
    if exclude_ambiguous:
        lower = lower.replace('l', '').replace('i', '')
        upper = upper.replace('O', '').replace('I', '')
        digits = digits.replace('0', '')

    # Customizable character pool
    char_pool = ""
    if include_lower:
        char_pool += lower
    if include_upper:
        char_pool += upper
    if include_digits:
        char_pool += digits
    if include_special:
        char_pool += specials

    if len(char_pool) == 0:
        raise ValueError("At least one character set must be included.")

    # Randomly generate a password
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

# Function to check password complexity and strength
def check_password_complexity(password):
    # Checking length
    if len(password) < 16:
        return "Password is too short. Must be at least 16 characters."
    
    # Checking for lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Checking for uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Checking for digits
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    
    # Checking for special characters
    if not re.search(r'[@#$%^&+=!]', password):
        return "Password must contain at least one special character."
    
    # If all conditions are met
    return "Password is strong and meets the requirements!"

# Function to rate the strength of the password
def rate_password_strength(password):
    length = len(password)
    unique_chars = len(set(password))

    # Calculate the entropy of the password
    entropy = calculate_entropy(password)
    
    # Password Strength Rating System (basic)
    if entropy < 40:
        strength = "Weak"
    elif entropy < 60:
        strength = "Moderate"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        'entropy': entropy,
        'unique_characters': unique_chars,
        'strength': strength,
        'length': length
    }

# Function to calculate entropy (Randomness) of the password
def calculate_entropy(password):
    char_space = len(set(password))  # Number of unique characters in the password
    length = len(password)           # Length of the password
    if char_space <= 1:
        return 0
    # Shannon Entropy formula: H(X) = log2(N^L)
    entropy = length * math.log2(char_space)
    return round(entropy, 2)

# Example usage:
generated_password = generate_password(length=20, include_upper=True, include_lower=True, include_digits=True, include_special=True)
print(f"Generated Password: {generated_password}")

# Check password complexity
complexity_result = check_password_complexity(generated_password)
print(f"Password Complexity Check: {complexity_result}")

# Rate password strength
strength_info = rate_password_strength(generated_password)
print(f"Password Strength: {strength_info['strength']}")
print(f"Entropy: {strength_info['entropy']}")
print(f"Unique Characters: {strength_info['unique_characters']}")
print(f"Password Length: {strength_info['length']}")

