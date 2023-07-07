"""
schwer

Vereinfachte Version von 17 und 4, in der der Spieler nur gegen sich selbst
spielt.
Spieler zieht solange Karten, bis er entscheidet, das Spiel zu beenden oder sein 
Kartenwert > 21 ist.
Wenn der Gesamtwert seiner Karten <= 21 und > 17, hat der Spieler gewonnen.
Anderenfalls hat er verloren.

Kartenwerte
2, 3, 4, 5, 6, 7, 8, 9, 10
Bube, Dame, König: 10
Ass 11

shuffle methode aus dem random Modul
es werden 4 Kartensätze in einem Spiel genutzt
"""
import random
'''
1. tatsächliches 17 + 4 einbauen
2. Anzahl der Player einstellen 
3. Gambling 
'''

# values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# colors = ["Pik", "Herz", "Kreuz", "Karo"]
# french_deck = [(color, value) for color in colors for value in values]
# play_deck = french_deck * 4

# playing = True
# player = 0
# cards = []

# random.shuffle(play_deck)

# while playing:   
#     print(cards)
#     action = input("+ für noch eine, - für keine karte mehr, q für quit ")
#     match action:
#         case "+":
#             card = play_deck.pop()
#             cards.append(card)
#             if sum(card[1] for card in cards) >= 22:
#                 print("Verloren")
#                 cards.clear()
#         case "-":
#             if sum(card[1] for card in cards) >= 17:
#                 print("Gewonnen")
#                 cards.clear()
#             elif sum(card[1] for card in cards) <= 16:
#                 print("mindestens Kartenwert 17")

#         case "q":
#             playing = False


values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
colors = ["Pik", "Herz", "Kreuz", "Karo"]
french_deck = [(color, value) for color in colors for value in values]

play_deck = french_deck * 4
winners = {}
players = {}
highest_value_players = []
playing = True
set_up = True
prize_pool = 0
end = 0



while set_up:
    gamestart = input("q zum Beenden ")
    if gamestart == "q":
        set_up = False
    else:
        player_count = int(input("Wie viele Spieler?: "))
        player_names = input("Wie sind die Spielername?: ").split(",")

        for n in range(player_count):
            player_name = player_names[n]
            players[player_name] = {"cards": [], "coins": 100, "game_round": 0, "betting": 0, "pause": 0}

    random.shuffle(play_deck)

    while playing:
        for player_name in players.keys():
            
            if players[player_name]["betting"] == 0:
                print("#" * 60)
                print(f"{player_name} dein Zug!")
                print(f"Du hast noch {players[player_name]['coins']}")
                bet = int(input("Wie viel möchtest du setzen? "))
                print("#" * 60)
                players[player_name]["coins"] -= bet
                players[player_name]["betting"] += 1
                players[player_name]["game_round"] += 1
                prize_pool += bet
                continue
            
            elif players[player_name]["game_round"] == 1:
                print("#" * 60)
                print(f"Im Topf sind Chips im Wert von {prize_pool}")
                print(f"{player_name} dein Zug!")
                action = input("+ gib mir eine Karte! oder q für quit game ")
                print("#" * 60)

            elif players[player_name]["game_round"] > 1:
                print("#" * 60)
                print(f"{player_name} deine Karten {players[player_name]['cards']}")
                action = input("+ gib mir eine Karte!, - Ich bleibe so!, q für quit game ")
                print("#" * 60)
            
            elif end == player_count:
                if player_name not in winners:
                    print(f"{player_name} hat diese Runde alles verspielt!")
                    players[player_name]["pause"] -= 1

                for player_name in winners:
                    total_values = [sum(card[1] for card in winner["cards"]) for winner in winners]
                    highest_value = max(total_values)
                    highest_value_players.append = [player for player in winners if sum(card[1] for card in player["cards"]) == highest_value]

                if len(highest_value_players) == 1:
                    winner_name = next(iter(highest_value_players))
                    print(f"Herzlichen Glückwunsch {winner_name} du hast {prize_pool} coins gewonnen!")
                    players[winner_name]["coins"] += prize_pool
                    players[player_name]["pause"] -= 1
                    prize_pool = 0
                    end = 0

                if len(highest_value_players) > 1:
                    print("Der Pott wurde gesplittet!")
                    for winner in highest_value_players:
                        winner_name = next(iter(winner))
                        print(f"{winner_name} hat {prize_pool / len(highest_value_players)} coins gewonnen!")
                        players[winner_name]["coins"] += prize_pool / len(highest_value_players)
                        players[player_name]["pause"] -= 1
                        prize_pool = 0
                        highest_value_players.clear()
                        end = 0
                
            match action:
                case "+":
                    if players[player_name]["pause"] > 0:
                        break
                    else:
                        card = play_deck.pop()
                        players[player_name]["cards"].append(card)
                        players[player_name]["game_round"] += 1

                        print(f"Gezogene Karte:{card}")
                        if sum(card[1] for card in players[player_name]["cards"]) >= 22:
                            print("Sorry, du bist raus für die Runde!")
                            players[player_name]["cards"].clear()
                            players[player_name]["game_round"] = 0
                            players[player_name]["pause"] += 1
                            end += 1

                case "-":
                    if players[player_name]["pause"] > 0:
                        break
                    else:
                        if sum(card[1] for card in players[player_name]["cards"]) < 17:
                            print("Du brauchst mindestens den Kartenwert 17!")

                        elif sum(card[1] for card in players[player_name]["cards"]) >= 17:
                            winners[player_name] = {"cards": []}
                            players[player_name]["cards"].clear()
                            players[player_name]["game_round"] = 0
                            players[player_name]["pause"] += 1
                            end += 1

                case "q":
                    playing = False
