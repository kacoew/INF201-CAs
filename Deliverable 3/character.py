"""
Object-oriented game simulator
Based on game_simulator_v1.py by Turid Torheim, NMBU, 2026
Owner: Person A (Task 1, Character-delen av Task 3, Task 4)

=====================================================================
OPPGAVEN
=====================================================================
Task 1 – Rett opp Character-klassen
  Problemet i startkoden: attack() endrer target._hp direkte. Det er
  dårlig skikk å endre et annet objekts private attributt. Hvert objekt
  skal selv passe på sin egen tilstand.
    * take_damage(amount): karakteren tar skade på SIN EGEN HP.
    * heal(amount): karakteren øker SIN EGEN HP.
    * attack(target): kaller target.take_damage(...) i stedet for å
      røre target._hp.
    * is_alive: read-only property, True hvis HP > 0, ellers False.
  Regel: HP skal alltid ligge mellom 0 og hp_max.

Task 3 – Character-delen
    * __init__ tar imot et valgfritt våpen (standard: ingen).
    * Har karakteren et våpen, kastes våpenets terning i attack().
      Ellers brukes base damage (self.damage).

Task 4 – Spesialiserte subklasser
  Warrior (forsvar):
    * Nytt attributt armor, standard 5.
    * Overstyr take_damage(): trekk armor fra innkommende skade før den
      brukes. Skaden kan ikke bli negativ (ellers ville angrep helbrede).
  Mage (ressurser):
    * Nye attributter mana og mana_max, begge standard 30.
    * Overstyr attack():
        - Mana >= 10: bruk 10 mana og gjør et magisk angrep med DOBBEL
          skade. Magi bruker IKKE våpen, selv om magen har et.
          (Tolkning å avklare: dobbel base damage, dvs. 2 * self.damage.)
        - Mana < 10: vanlig angrep (med våpen hvis utstyrt), og få
          tilbake 5 mana (ikke over mana_max).

=====================================================================
BEGREPER DU TRENGER
=====================================================================
  * Innkapsling: _hp med understrek betyr "privat, ikke rør utenfra".
    Lesing skjer via property-en hp, endring kun via take_damage/heal.
  * @property uten setter er read-only: forsøk på å sette verdien gir
    AttributeError. Det er nettopp det dere vil for hp og is_alive.
  * Arv ("er en"): en Warrior ER EN Character. Den får alle metodene
    gratis og overstyrer bare det som skal være annerledes.
  * super(): bruk super().__init__(...) i subklassene så Character
    setter opp navn, HP osv. – ikke kopier den koden. I overstyrte
    metoder kan super().take_damage(...) / super().attack(...) gjenbruke
    logikken i foreldreklassen.
  * Polymorfisme: attack() kaller target.take_damage(). Er target en
    Warrior, kjøres Warrior sin versjon automatisk. Angriperen trenger
    ikke vite hvilken type målet er.

=====================================================================
FREMGANGSMÅTE
=====================================================================
  1. Task 1 først, i rekkefølge:
       a. take_damage: trekk fra, og sørg for at HP ikke går under 0.
       b. heal: legg til, og sørg for at HP ikke går over hp_max.
          Vurder hva som skal skje med negative tall (ValueError?).
       c. is_alive: property som sammenligner HP med 0.
       d. attack: finn skaden, og la målet ta skaden selv.
       e. Fiks __repr__ (se TODO der).
  2. Task 3: lagre våpenet i __init__ og skriv hjelpemetoden
     roll_attack_damage(). Den svarer på "hvor mye skade gjør jeg nå?"
     og brukes av attack(). Da kan Mage gjenbruke den.
     Tips: Person B sin Weapon er kanskje ikke ferdig ennå. Du kan teste
     med et enkelt hjemmelaget objekt som har en roll_damage()-metode.
  3. Task 4, Warrior: __init__ med super() + armor, deretter
     take_damage som reduserer skaden og lar super() gjøre resten.
  4. Task 4, Mage: __init__ med super() + mana/mana_max, deretter
     attack med de to grenene. Pass på at mana aldri går over mana_max.
  5. Test hver metode alene før dere kobler på Battle:
       - En karakter med 100 HP som tar 150 skade ender på 0, ikke -50.
       - Heal på en karakter med full HP gir fortsatt hp_max.
       - is_alive er False ved 0 HP, og kan ikke settes utenfra.
       - Å sette hp direkte utenfra gir AttributeError.
       - En Warrior med armor 5 som tar 3 skade mister 0 HP.
       - En Mage gjør 20, 20, 20 skade (bruker 30 mana), deretter vanlig
         angrep og får +5 mana hver gang til den har 10 igjen.
       - En Mage med våpen bruker IKKE våpenet når den kaster magi.
"""