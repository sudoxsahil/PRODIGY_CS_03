import re
from zxcvbn import zxcvbn

def regex_check(password):
    checks = {
        'Length (min 8)': len(password) >= 8,
        'Uppercase': bool(re.search(r'[A-Z]', password)),
        'Lowercase': bool(re.search(r'[a-z]', password)),
        'Digit': bool(re.search(r'\d', password)),
        'Special Char': bool(re.search(r'[\W_]', password)),
    }

    print("\n🔍 Regex Checks:")
    for key, passed in checks.items():
        print(f"{'✅' if passed else '❌'} {key}")
    
    if all(checks.values()):
        print("✅ Meets basic complexity rules.")
    else:
        print("⚠️  Does not meet all basic rules.")

def zxcvbn_check(password):
    print("\n🔐 zxcvbn Analysis:")
    result = zxcvbn(password)
    score = result['score']
    crack_time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
    feedback = result['feedback']

    score_text = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }

    print(f"🔢 Score: {score} ({score_text[score]})")
    print(f"⏳ Estimated time to crack: {crack_time}")

    if feedback['warning']:
        print(f"⚠️ Warning: {feedback['warning']}")
    if feedback['suggestions']:
        print("💡 Suggestions:")
        for suggestion in feedback['suggestions']:
            print(f" - {suggestion}")

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to evaluate: ")

    regex_check(password)
    zxcvbn_check(password)

if __name__ == "__main__":
    main()
