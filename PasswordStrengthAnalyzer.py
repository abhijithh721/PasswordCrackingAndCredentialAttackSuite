import math
import re

def password_strength_analyzer():
    print("--- Password Strength Analyzer ---")
    password = input("Enter a password to analyze: ")
    
    # 1. Complexity Check 
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # 2. Entropy Calculation 
    character_pool = 0
    if has_lower: character_pool += 26
    if has_upper: character_pool += 26
    if has_digit: character_pool += 10
    if has_special: character_pool += 32
    
    # Entropy Formula: log2(pool^length)
    if character_pool > 0:
        entropy = length * math.log2(character_pool)
    else:
        entropy = 0

    # 3. Strength Rating
    print(f"\n--- Analysis Results ---")
    print(f"Length: {length} characters")
    print(f"Entropy: {round(entropy, 2)} bits")
    
    if entropy < 40:
        rating = "Very Weak (Easily Crackable)"
    elif entropy < 60:
        rating = "Medium (Vulnerable to brute-force)"
    else:
        rating = "Strong"
        
    print(f"Strength Rating: {rating}")
    
    # 4. Improvement Recommendations (Requirement 48)
    print("\nRecommendations:")
    if length < 12:
        print("- Increase length to at least 12-16 characters.")
    if not (has_upper and has_lower and has_digit and has_special):
        print("- Mix uppercase, lowercase, numbers, and symbols.")
    if entropy < 60:
        print("- Avoid common words or simple patterns.")

if __name__ == "__main__":
    password_strength_analyzer()
