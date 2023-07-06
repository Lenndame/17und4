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

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
colors = ["Pik", "Herz", "Kreuz", "Karo"]
french_deck = [(color, value) for color in colors for value in values]

playing = True
# set_up = True
dealer = 0
player = 0
cards = []
# while set_up:
#     player_count = int(input("wie viele spieler?: "))
#     player_names = input("wie heißt der spieler?: ")
#     for i in players:
#     players = {}

random.shuffle(french_deck)

while playing:   
    print(cards)
    action = input("+ für noch eine, - für keine karte mehr, q für quit ")
    match action:
        case "+":
            card = french_deck.pop()
            cards.append(card)
            if sum(cards[1]) >= 22:
                print("Verloren")
        case "-":
            if sum(cards([][1])) > 22:
                print("Verloren")
            if sum(cards([][1])) >= 17:
                print("Gewonnen")

        case "q":
            playing = False

