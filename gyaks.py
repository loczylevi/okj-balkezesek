class Balkezesek:
    def __init__(self,sor):
        nev,elso,utolso,suly,magassag = sor.strip().split(";")
        self.nev = nev
        self.elso = elso
        self.utolso = utolso
        self.suly = int(suly)
        self.magassag = int(magassag)
        self.utolso_ev = int(utolso[0:4])
        self.elso_ev = int(elso[0:4])
        self.utolso_honap = int(utolso[5:7])
        
with open("balkezesek.csv","r",encoding="latin2") as f:
    fejlec = f.readline()
    lista = [Balkezesek(sor) for sor in f]
    
print(f"3.feladat: {len(lista)}")

utoljara_oktoberben = [sor for sor in lista if sor.utolso_ev == 1999 and sor.utolso_honap == 10]

print("4.feladat:")

#[print(f"    {sor.nev}, {sor.magassag * 2.54} cm") for sor in utoljara_oktoberben]

for sor in utoljara_oktoberben:
    magassag = sor.magassag * 2.54
    magassag = round(magassag, 1)
    magassag = str(magassag)
    magassag = magassag.replace('.',',')
    print(f"       {sor.nev}, {magassag} cm")
    
print("5.feladat")
bekeres = int(input("Kérek egy 1990 és 1999 közötti évszámot!: "))
while True:
    if 1990 <= bekeres <= 1999:
        break
    else:
        bekeres = int(input("Hibás adat!Kérek egy 1990 és 1999 közötti évszámot!: "))

#  ༼ つ ◕_◕ ༽つ

atlag_suly_x_evben = [sor.suly for sor in lista if sor.elso_ev <= bekeres <= sor.utolso_ev]
ossz = sum(atlag_suly_x_evben)
atlag = ossz / len(atlag_suly_x_evben)
atlag = round(atlag, 2)
atlag = str(atlag)
atlag = atlag.replace('.',',')
print(f"6.feladat: {atlag} font")