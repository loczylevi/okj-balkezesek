#név;első;utolsó;súly;magasság
with open("balkezesek.csv", "r",encoding="latin2") as f:
    elso_sor = f.readline()
    lista = []
    for sor in f:
        lista.append(sor.strip().split(";"))
        
    #lista = [sor.strip().split(';') for sor in f]

print(f"3.feladat: {len(lista)}")

utoljara_oktoberben = [sor for sor in lista if sor[2][0:4] == "1999" and sor[2][5:7] == "10"]
print("4.feladat: ")
#[print(f"    {sor[0]}, {int(sor[4]) * 2.54} cm") for sor in utoljara_oktoberben]   # egyszerűbb megoldás

# két tizedesre kerekités és string finomitások 
for sor in utoljara_oktoberben:
    magassag = int(sor[4]) * 2.54         # 1 inch = 2,54 cm 
    kerekites = round(magassag, 1)
    finomitas = str(kerekites).replace('.',',')
    print(f"       {sor[0]}, {finomitas} cm")

print("5.feladat: ")
bekeres = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
while True:
    if 1990 <= bekeres <= 1999:
        break
    else:
        bekeres = int(input("Hibás adat!Kérek egy 1990 és 1999 közötti évszámot!: "))
        
magassagok_x_evben = [int(sor[3]) for sor in lista if int(sor[1][0:4]) <= bekeres <= int(sor[2][0:4])]

ossz = sum(magassagok_x_evben)
atlag = ossz / len(magassagok_x_evben)

kerekites_magas = round(atlag, 2)
finomitas2 = str(kerekites_magas).replace('.',',')
print(f"6.feladat: {finomitas2} font")

#    ༼ つ ◕_◕ ༽つ      uwu
