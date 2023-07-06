mport random

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
colors = ["Pik", "Herz", "Kreuz", "Karo"]
french_deck = [(color, value) for color in colors for value in values]

play_deck = french_deck * 4

players = {}

playing = True
set_up = True

hand = []

while set_up:
    gamestart = input("q zum Beenden ")
    if gamestart == "q":
        set_up = False
    else:
        player_count = int(input("Wie viele Spieler?: "))
        player_names = input("Wie sind die Spielername?: ").split(",")

        for n in range(player_count):
            player_name = player_names[n]
            players[player_name] = {"cards": [], "points": 0, "game_round": 0}

    random.shuffle(french_deck)

    while playing:
        for player_name in players.keys():
            if players[player_name]["game_round"] == 0:
                print(f"{player_name} dein Zug!")

            else:
                print(f"{player_name} deine Karten {players[player_name]['cards']}")
            action = input("+ gib mir eine Karte!, - Ich bleibe so!, q für quit ")
            
            match action:

                case "+":
                    card = french_deck.pop()
                    players[player_name]["cards"].append(card)
                    players[player_name]["game_round"] += 1

                    print(f"Gezogene Karte:{card}")
                    if sum(card[1] for card in players[player_name]["cards"]) >= 22:
                        print("Sorry, du hast verloren!")
                        players[player_name]["cards"].clear()

                case "-":
                    if sum(card[1] for card in players[player_name]["cards"]) >= 17:
                        players[player_name]["cards"].clear()
                        print("Herzlichen Glückwunsch, du hast gewonnen!")
                        players[player_name]["points"] += 1
                    if sum(card[1] for card in players[player_name]["cards"]) < 17:
                        print("Du brauchst mindestens den Kartenwert 17!")

                case "q":
                    playing = False
