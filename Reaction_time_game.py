import random
import time
import keyboard
import os

peliaika = 3 #seconds
initial_peliaika = 3
lisäpiste = 100
pelaajan_pisteet = 0


def peliohjeet():
    print("Game instructions:")
    print("Game buttons: 'a','s','d','f'")
    valmis = input("Press 'Enter' to start the game!")
    return valmis

def kysy(peliaika, kysytty_merkki):
    # resettaa ajastimet
    juokseva_aika_alku = 0
    juokseva_aika_loppu = 0
    # aloita ajastin
    juokseva_aika_alku = time.perf_counter()

    while True:
        event = keyboard.read_event()
        juokseva_aika_loppu = time.perf_counter()
        vastaus_aika = juokseva_aika_loppu - juokseva_aika_alku
        if vastaus_aika < peliaika:
            if event.event_type == keyboard.KEY_DOWN and event.name == kysytty_merkki:
                return True
            elif event.event_type == keyboard.KEY_DOWN and event.name != kysytty_merkki:
                return False
        else:
            print("Too slow, time ends!")
            return False
  
def kysy_uusi_peli():
    __puhdista_kayttaja_input()
    while True:
        valinta = input("Do you want to play again?, Yes = 1, No = 0\n")
        if valinta == "1":
            uusi_peli = True
            return uusi_peli
        elif valinta == "0":
            uusi_peli = False
            return uusi_peli
        else:
            print("Only 1 or 0 is valid answer")

def __puhdista_kayttaja_input():
    for _ in range(35):
        keyboard.press_and_release('left')
        time.sleep(0.02)
        keyboard.press_and_release('delete')

def pelaa(peliaika, pelaajan_pisteet):

    pistetaulukko = []
    uusi_peli = 1

    while True:

        peliaika = initial_peliaika
        pelaajan_pisteet = 0

        while uusi_peli:
            kysytty_merkki = random.choice(['a', 's', 'd', 'f'])
            peliaika = round(peliaika, 2)
            print(f"Press '{kysytty_merkki}', you have {peliaika} seconds")

            painallus_oikein = kysy(peliaika, kysytty_merkki)

            if painallus_oikein:
                print("Correct!")
                pelaajan_pisteet += int(lisäpiste) + int(pelaajan_pisteet)*0.1
                pelaajan_pisteet = round(pelaajan_pisteet, 1)
                print(pelaajan_pisteet)
                peliaika *= 0.9
            else:
                print("Game over!")
                pistetaulukko.append(pelaajan_pisteet)
                break

        # Sort the scoreboard in descending order
        pistetaulukko = sorted(pistetaulukko, reverse=True)

        print(f"Your latest score: {pelaajan_pisteet}")
        print(f"Scoreboard: {pistetaulukko}")

        print("--------")

        uusi_peli = kysy_uusi_peli()
        if not uusi_peli:
            return
        

if __name__ == "__main__":
    peliohjeet()
    pelaa(peliaika, pelaajan_pisteet)