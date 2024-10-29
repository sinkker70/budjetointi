# Tähän pitäisi tulla koodia: ...

# Vuokra
# Vakuutukset
# Kouluruokailu
# Sähkö
# Liikkuminen
# Voit tallentaa nämä tiedot esimerkiksi sanakirjaan (dictionary), jossa avaimet ovat kululajien nimiä ja arvot ovat kulujen summia.

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

summa = 0
for key, value in budjetti.items(): 
    summa += value

print(f"Kuukauden budjettisi on:  {summa}")