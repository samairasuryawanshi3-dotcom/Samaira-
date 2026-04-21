import random

# A simple Ludo race for 2 players
def start_game():
    print("=== Welcome to Samaira's Ludo Game ===")
    p1_pos = 0
    p2_pos = 0
    target = 20  # First to 20 wins!

    while p1_pos < target and p2_pos < target:
        # Player 1 Turn
        input("\nPlayer 1: Press Enter to roll...")
        roll = random.randint(1, 6)
        p1_pos += roll
        print(f"🎲 Rolled a {roll}! You are now at: {p1_pos}")
        
        if p1_pos >= target:
            print("🎉 PLAYER 1 WINS!")
            break

        # Player 2 Turn
        input("\nPlayer 2: Press Enter to roll...")
        roll = random.randint(1, 6)
        p2_pos += roll
        print(f"🎲 Rolled a {roll}! You are now at: {p2_pos}")
        
        if p2_pos >= target:
            print("🎉 PLAYER 2 WINS!")
            break

    print("\nThanks for playing!")

start_game()
