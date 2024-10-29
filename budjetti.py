# Tähän pitäisi tulla koodia: ...
# Vaihe 2: Mukautettavien budjettikohteiden lisääminen
# Laajenna ohjelmaa siten, että käyttäjä voi lisätä omia budjettikohteita.
# Ohjelman tulee pyytää käyttäjää antamaan uuden kuluerän nimi ja siihen budjetoitu summa.
# Nämä käyttäjän lisäämät budjettikohteet tallennetaan samaan rakenteeseen, johon myös ennakkoon määritellyt kohteet on tallennettu.
# monirivinen kursori oli: Ctrl + Alt + nuoli alaspäin

# Vaihe 3: Budjettikohteiden muokkaaminen
# Laajenna ohjelmaa siten, että käyttäjä voi muokata aiemmin syöttämiään budjettikohteita.
# Anna käyttäjälle mahdollisuus valita, mitä budjettikohdetta hän haluaa muokata, ja syöttää uusi summa.

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

# kokonaisbudjetin laskenta ja tulostus
def tulostaBudjetti(budjetti): 
    
    print("---------")
    print("Kuluerät: ")
    summa = 0
    for key, value in budjetti.items():
        print(f"{key}: {value}")
        summa += budjetti[key]
    print("==================================")
    print(f"Kuukauden budjettisi on:  {summa}")

def lisaaKulu(budjetti): 
    syote = input("Anna uuden kuluerän nimi: ")
    budjetti[syote] = int(input(f"Anna {syote}: "))

def muokkaa(budjetti): 
    for key, value in budjetti.items(): 
        print(key) 
    syote = input("Mitä haluat muokata?")
    budjetti[syote] = int(input(f"Anna {syote}: "))


print("-------")
while True: 
    print("Komennot:")
    print("(l)isää kulu")
    print("(m)uokkaa kulua")
    print("(t)ulosta budjetti")
    print("(q) poistu ohjelmasta")
    syote = input("Komento: ")
    match syote: 
        case 'l': 
            lisaaKulu(budjetti)
        case 'm': 
            muokkaa(budjetti)
        case 't':
            tulostaBudjetti(budjetti)
        case 'q': 
            break
        case __:
            print('Tuntematon komento')
            break


    