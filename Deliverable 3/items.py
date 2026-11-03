"""
Items that characters can hold
Owner: Person B (Task 3, Weapon-delen)

=====================================================================
OPPGAVEN (Task 3)
=====================================================================
Lag en Weapon-klasse som bruker Dice til å regne ut skade. Modulen heter
items.py (ikke weapons.py) slik at den senere kan utvides med andre ting
en karakter kan bære, f.eks. Potion eller Shield.

Krav fra oppgaveteksten:
  * Weapon har attributtene name og damage_dice (et Dice-objekt).
  * roll_damage() kaster våpenets terning og returnerer skaden.

Den andre halvdelen av Task 3 (at Character tar imot et våpen og bruker
det i attack()) gjøres av Person A i character.py.

=====================================================================
BEGREPER DU TRENGER
=====================================================================
  * Komposisjon ("har en"): et Weapon HAR EN Dice. Weapon arver ikke fra
    Dice, det inneholder en Dice og delegerer kastet til den. Senere vil
    en Character HA ET Weapon. Det er dette oppgaven kaller
    "object composition".
  * Delegering: Weapon trenger ikke vite hvordan en terning fungerer,
    bare at den har en roll()-metode. Da kan dere bytte terning uten å
    endre Weapon.
  * Type hints: damage_dice: Dice dokumenterer hva som forventes, men
    Python sjekker det ikke selv. Vurder om dere vil sjekke typen med
    isinstance og gi TypeError hvis noen sender inn noe annet.

=====================================================================
FREMGANGSMÅTE
=====================================================================
  1. Vent ikke på at Dice er ferdig: grensesnittet (roll() -> int) er
     avtalt, så du kan skrive Weapon parallelt.
  2. Skriv __init__: lagre navnet og terningen som attributter.
     (Valgfritt) sjekk at damage_dice faktisk er en Dice.
  3. Skriv roll_damage(): la terningen gjøre jobben og returner
     resultatet. Ingen egen tilfeldighetslogikk her.
  4. Skriv __repr__ slik at det er lett å se våpenet i notatboken,
     f.eks. med navn og terning (Dice sin __repr__ gjør resten).
  5. Lag noen eksempelvåpen dere kan bruke i kampene, for eksempel
     en dolk med liten terning og et tohåndssverd med stor terning.
     Velg verdier som gir interessante kamper mot base damage 10.
  6. Test:
       - roll_damage() gir alltid et tall mellom 1 og antall sider.
       - To våpen kan dele samme Dice-objekt uten problemer.
       - repr viser både navn og terning.
"""
