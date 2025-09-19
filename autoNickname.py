import random

nickname_history = []

def combine_default(name1, name2):
    return name1[:2] + name2[-2:]

def combine_half(name1, name2):
    half1 = len(name1) // 2
    half2 = len(name2) // 2
    return name1[:half1] + name2[half2:]

def combine_random(name1, name2):
    combined = "".join(random.choice(name1 + name2) for _ in range(4))
    return combined.capitalize()

def combine_three_letters(name1, name2):
    return name1[:3] + name2[:3]

def combine_reversed(name1, name2):
    return name1[::-1][:2] + name2[::-1][:2]

def generate_meaning(nickname):
    meanings = [
        "the Brave", "the Mysterious", "the Kind",
        "the Clever", "the Strong", "the Dreamer"
    ]
    return f"{nickname} {random.choice(meanings)}"

def generate_nickname(name1, name2):
    styles = [
        combine_default,
        combine_half,
        combine_random,
        combine_three_letters,
        combine_reversed
    ]
    nickname = random.choice(styles)(name1, name2)
    nickname_history.append(nickname)
    return nickname

def main():
    print("🎉 Welcome to the Nickname Generator Bot 🎉")

    while True:
        name1 = input("Enter the first name: ").strip().capitalize()
        name2 = input("Enter the second name: ").strip().capitalize()

        if not name1 or not name2:
            print("⚠️ Please enter valid names.")
            continue

        # Generate multiple nickname suggestions
        print("\nHere are some nickname suggestions:")
        for _ in range(3):
            nick = generate_nickname(name1, name2)
            print(f"👉 {nick} ({generate_meaning(nick)})")

        # Show history
        print("\nNickname History:", ", ".join(nickname_history))

        choice = input("\nDo you want to try again? (y/n): ").lower()
        if choice != 'y':
            print("Goodbye! Thanks for playing 👋")
            break

if __name__ == "__main__":
    main()
