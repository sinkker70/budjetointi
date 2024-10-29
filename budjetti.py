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

# sanakirjan alustaminen
budjetti = {
    "Vuokra": 0, 
    "Vakuutukset": 0,
    "Kouluruokailu": 0, 
    "Sähkö": 0, 
    "Liikkuminen": 0
}

print("Hei, anna budjettikohteet ja lasken kuukauden kokonaisbudjetin!")
print("---------------------")

for key, value in budjetti.items():
    budjetti[key] = int(input(f"Anna {key}: "))

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


    