import re

def check_password_strength(password: str):
    
    length = len(password)

    # Flags for character types
    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", password))

    score = 0
    suggestions = []

    # 1. Length
    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8–12 characters.")

    # 2. Variety
    if has_lower and has_upper:
        score += 1
    else:
        suggestions.append("Mix uppercase and lowercase letters.")

    if has_digit:
        score += 1
    else:
        suggestions.append("Add at least one number.")

    if has_symbol:
        score += 1
    else:
        suggestions.append("Add at least one special symbol (!,@,#,$).")

    # Convert score (0–5) to star rating
    stars = min(score, 5)
    rating_text = "★" * stars + "☆" * (5 - stars)

    # Add qualitative feedback
    if stars >= 4:
        quality = "Good"
    elif stars == 3:
        quality = "Average"
    else:
        quality = "Poor"

    return stars, rating_text, quality, suggestions


def main():
    print("🔐 Password Strength Checker (Star Rating)\n")

    while True:
        password = input("Enter a password: ")
        stars, rating_text, quality, suggestions = check_password_strength(password)

        print(f"\nPassword Rating: {rating_text}  ({stars}/5 Stars, {quality})")

        if suggestions:
            print("Suggestions to improve:")
            for s in suggestions:
                print(" •", s)
        else:
            print("Great job! ✅ Strong password.")

        # Stop only when password is 4 or 5 stars
        if stars >= 4:
            print("\n✅ Accepted! Your password is strong enough.")
            break
        else:
            print("\n⚠️ Try again with a stronger password.\n")


if __name__ == "__main__":
    main()
