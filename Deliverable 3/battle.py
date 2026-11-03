"""
Turn-based combat manager
Owner: Person B (Task 5)

=====================================================================
OPPGAVEN (Task 5)
=====================================================================
Lag en Battle-klasse som styrer en turbasert kamp mellom to karakterer.

Krav fra oppgaveteksten:
  * Battle lages med hero og enemy (begge Character-objekter, eller
    subklasser som Warrior og Mage).
  * play_round(): hero angriper enemy. Hvis enemy fortsatt lever,
    angriper enemy hero.
  * simulate_battle(): en while-løkke som spiller runder til en av dem
    ikke lever lenger.

=====================================================================
BEGREPER DU TRENGER
=====================================================================
  * Battle er en "manager"-klasse: den eier ingen kampregler selv, men
    kaller metodene karakterene allerede har (attack, is_alive, hp).
    All logikk for skade, armor og mana ligger i character.py.
  * Polymorfisme: Battle trenger ikke vite om noen er Warrior eller Mage.
    attack() og take_damage() gjør automatisk det riktige.
  * while-løkke med en betingelse: løkken går så lenge BEGGE lever.

=====================================================================
FREMGANGSMÅTE
=====================================================================
  1. Du trenger ikke vente på Person A: lag midlertidig en enkel
     testklasse med attack(), hp og is_alive for å teste Battle.
  2. __init__: lagre hero og enemy. En rundeteller er nyttig for
     utskrift og for å vise hvor lange kampene ble.
  3. play_round(): øk rundetelleren, hero angriper, og BARE hvis enemy
     fortsatt lever angriper enemy tilbake. En død karakter skal ikke
     kunne slå.
     (Valgfritt) Skriv ut hva som skjer, f.eks. rundenummer og HP etter
     hvert angrep. Det gjør kampene i notatboken mye lettere å følge.
  4. simulate_battle(): kjør play_round() i en løkke så lenge begge
     lever. Returner vinneren, så notatboken kan telle seire.
  5. Tenk på kanttilfeller:
       - Uendelig løkke: to Warriors med armor >= motstanderens skade
         gjør aldri skade på hverandre. Vurder en maks rundegrense
         (f.eks. et valgfritt argument) og hva som da regnes som utfall.
       - Hva hvis en karakter allerede er død før kampen starter?
  6. Test og bruk i notatboken:
       - Character mot Character uten våpen (forutsigbar, uten terning).
       - Med og uten våpen.
       - Warrior mot Mage, og bytt hvem som er hero (den som slår først
         har en fordel).
       - Kjør f.eks. 1000 kamper og tell seire for å sammenligne typene.
         Husk å lage nye karakterer for hver kamp – ellers starter de
         neste kamp med 0 HP.
"""

