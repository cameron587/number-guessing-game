import random

#intro
print("\n")
print("Welcome to the number guessing game!\n")

#variables
number = random.randint (1, 100)
name = input("What is your name? ")
tries = 0

#guessing code
print("Guess a number (1-100)")
guess = int(input(""))

while guess != number:
    tries += 1

    if guess < number:
        print("Too low!\n")

    elif guess > number:
        print("Too high!\n")

    guess = int(input("Try again: "))
    print("\n")

else:
    tries += 1
    print(f"Correct! You got it in {tries} tries!")

#file saving
# Save new score
with open("high_scores.txt", "a") as f:
    f.write(f"{name}:{tries}\n")

# Read all scores
with open("high_scores.txt", "r") as f:
    lines = f.readlines()

# Convert to list of (name, score)
scores = []
for line in lines:
    try:
        player, attempt = line.strip().split(":")
        scores.append((player, int(attempt)))
    except:
        continue  # skip any bad lines

# Sort by score (ascending)
scores.sort(key=lambda x: x[1])

# Show top 5
print("\n🏆 Top 5 Scores:")
for i, (player, score) in enumerate(scores[:5], start=1):
    print(f"{i}. {player} - {score} tries")