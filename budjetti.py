# Tähän pitäisi tulla koodia: ...
# Vaihe 2: Mukautettavien budjettikohteiden lisääminen
# Laajenna ohjelmaa siten, että käyttäjä voi lisätä omia budjettikohteita.
# Ohjelman tulee pyytää käyttäjää antamaan uuden kuluerän nimi ja siihen budjetoitu summa.
# Nämä käyttäjän lisäämät budjettikohteet tallennetaan samaan rakenteeseen, johon myös ennakkoon määritellyt kohteet on tallennettu.
# monirivinen kursori oli: Ctrl + Alt + nuoli alaspäin

budjetti = {
    "Vuokra": 0, 
    "Vakuutukset": 0,
    "Kouluruokailu": 0, 
    "Sähkö": 0, 
    "Liikkuminen": 0
}

print("Hei, anna budjetti-kohteet ja lasken kuukauden kokonaisbudjetin!")
print("---------------------")

for key, value in budjetti.items():
    budjetti[key] = int(input(f"Anna {key}: "))

print("-------")
print("Syötä 'q', jos haluat lopettaa kulujen syöttämisen.")
while True: 
    syote = input("Anna uuden kuluerän nimi: ")
    if syote == 'q':
        break
    budjetti[syote] = int(input(f"Anna {syote}: "))

# kokonaisbudjetin laskenta
summa = 0
for key, value in budjetti.items():
    summa += budjetti[key]

print(f"Kuukauden budjettisi on:  {summa}")