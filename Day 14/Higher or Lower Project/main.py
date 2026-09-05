import random

data = [
    {"name": "Cristiano Ronaldo", "followers": 600},
    {"name": "Lionel Messi", "followers": 500},
    {"name": "Taylor Swift", "followers": 280},
    {"name": "Elon Musk", "followers": 200},
    {"name": "Selena Gomez", "followers": 420},
    {"name": "Ariana Grande", "followers": 380},
]

score = 0
game_over = False

while not game_over:

    person_a = random.choice(data)
    person_b = random.choice(data)

    while person_a == person_b:
        person_b = random.choice(data)

    print("\n" + "=" * 40)
    print(f"A: {person_a['name']}")
    print("VS")
    print(f"B: {person_b['name']}")

    answer = input(
        "Who has more followers? Type A or B: "
    ).upper()

    if person_a["followers"] > person_b["followers"]:
        correct_answer = "A"
    else:
        correct_answer = "B"

    if answer == correct_answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True