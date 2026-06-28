import random

print("=== MAFIA GAME ===")


num_players = int(input("How many players? (Minimum 4): "))

while num_players < 4:
    num_players = int(input("Please enter at least 4 players: "))


players = []

for i in range(num_players):
    name = input(f"Enter Player {i+1} name: ")
    players.append(name)


mafia = random.choice(players)

alive = players.copy()
round_number = 1

print("\nThe game begins!")

while True:

    print("\n========================")
    print(f"ROUND {round_number}")
    print("========================")


    print("\nNight falls...")

    possible_victims = alive.copy()
    possible_victims.remove(mafia)

    if len(possible_victims) == 0:
        print("Only the Mafia remains.")
        print("Mafia Wins!")
        break

    victim = random.choice(possible_victims)

    print(f"{victim} was eliminated during the night.")
    alive.remove(victim)


    if mafia not in alive:
        print("\nVillagers Win!")
        break

    if len(alive) == 2:
        print("\nMafia Wins!")
        break


    print("\nPlayers still alive:")

    for player in alive:
        print("-", player)

    print("\nVote someone out.")

    vote = input("Enter player's name: ")

    while vote not in alive:
        vote = input("That player isn't alive. Try again: ")

    alive.remove(vote)

    print(f"{vote} has been voted out.")

    if vote == mafia:
        print("\nThe Mafia has been caught!")
        print("Villagers Win!")
        break

    if len(alive) == 2:
        print("\nOnly two players remain.")
        print("Mafia Wins!")
        break

    round_number += 1

print("\nGame Over!")
print("The Mafia was:", mafia)