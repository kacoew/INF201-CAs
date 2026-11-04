"""
Dice class for the battle simulator
Owner: Person B (Task 2)

=====================================================================
OPPGAVEN (Task 2)
=====================================================================
I dag gjør karakterene alltid like mye skade. Vi vil ha tilfeldighet,
og lager derfor en egen klasse som modellerer en terning. Weapon (Task 3)
skal senere "ha en" Dice og bruke den til å regne ut skade.

Krav fra oppgaveteksten:
  * Dice kan ha n sider, der n >= 2. Standard er 6 sider.
  * roll() kaster terningen med random.randint(1, self.sides).
  * __repr__ gir en tekst som ser ut som "Dice(sides=6)".
  * __call__ gjør at objektet kan kalles som en funksjon, så et kall på
    d20 selv gir samme resultat som d20.roll().

=====================================================================
BEGREPER DU TRENGER
=====================================================================
  * Klasse og instans: Dice er "oppskriften", Dice(sides=20) er én
    konkret terning med 20 sider.
  * Validering i __init__: et objekt bør aldri kunne lages i en ugyldig
    tilstand. En terning med 1 eller 0 sider gir ikke mening, så stopp
    det med en ValueError allerede når objektet lages.
  * Spesialmetoder (dunder-metoder):
      - __repr__ bestemmer hva du ser når du skriver objektet i
        notatboken eller printer en liste med terninger.
      - __call__ kjøres når du skriver objektnavnet etterfulgt av ().
    Dokumentasjon: https://docs.python.org/3/reference/datamodel.html#object.__call__

=====================================================================
FREMGANGSMÅTE
=====================================================================
  1. Skriv __init__: sjekk at sides er et heltall >= 2, ellers ValueError
     med en tydelig melding. Lagre verdien som et attributt.
  2. Skriv roll(): returner et tilfeldig heltall mellom 1 og antall
     sider (begge inkludert). random.randint er inkludert i begge ender.
  3. Skriv __call__: den skal ikke inneholde egen logikk, bare gjenbruke
     roll(). Da har du kun ett sted å endre hvis reglene endres.
  4. Skriv __repr__: følg formatet fra oppgaveteksten nøyaktig.
  5. Test (i notatboken eller nederst i fila):
       - En standardterning har 6 sider.
       - 1000 kast med en 6-sidet terning gir bare verdier fra 1 til 6,
         og alle seks verdiene dukker opp.
       - Å kalle objektet direkte gir et tall i samme intervall som roll().
       - Å lage en terning med 1 side gir ValueError.
       - repr av en 20-sidet terning er nøyaktig "Dice(sides=20)".
  6. Tips til notatboken: random.seed(...) gjør kastene reproduserbare,
     nyttig når dere skal vise et eksempel i PDF-en og videoen.
"""

import random


class Dice:

    def __init__(self, sides: int = 6) -> None:
        '''
        Initialises the Dice

        Args:
            sides(int): number of sides om the dice, default = 6
        '''
        if sides < 2:
            raise ValueError('Number of sides must be 2 or more')
        self.sides = sides

    def roll(self) -> int:
        '''Returns a random number between 1 and the number of sides'''
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        '''Representation of Dice object'''
        return f'Dice(sides={self.sides})'

    def __call__(self):
        '''Rolls the dice when the object is called as a function'''
        return self.roll()
