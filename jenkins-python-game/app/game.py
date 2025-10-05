import random
import sys


def play_round(secret=None, guess_provider=None):
    """Play one round of number guessing.

    Inputs: optional secret int, optional guess_provider function that yields guesses.
    Output: dict with keys: attempts, success, secret
    """
    if secret is None:
        secret = random.randint(1, 100)

    attempts = 0
    if guess_provider is None:
        def prompt():
            return int(input("Guess a number between 1 and 100: "))
        guess_provider = prompt

    while True:
        attempts += 1
        try:
            guess = int(guess_provider())
        except Exception:
            return {"attempts": attempts, "success": False, "secret": secret}

        if guess == secret:
            return {"attempts": attempts, "success": True, "secret": secret}
        elif guess < secret:
            print("Too low")
        else:
            print("Too high")


if __name__ == "__main__":
    result = play_round()
    if result["success"]:
        print(f"You won in {result['attempts']} attempts!")
    else:
        print("Game ended.")
