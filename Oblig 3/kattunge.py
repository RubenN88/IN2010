def main():
    katt_start = int(input()) #forste input er der katten sitter
    forelder_map = {} #lager en ordbok som mapper hvert barn (nokkel) til sin forelder (verdi)

    while True:
        linje = input() #tar input fra bruker etter at katten er plassert
        if linje.strip() == "-1": #om input på et tidspunkt er -1 saa bryter vi ut av lokka
            break
    
        num = list(map(int, linje.strip().split())) #gjor om input til en liste med int, samt stripper og splitter
        if len(num) >= 2: #lengden paa input maa vaere >= 2 
            forelder = num[0] #foreldre settes til inputens forste verdi (num[0])
            barn = num[1:] #barn settes til alle verdier etter foreldre (num[1:])

        for i in barn: #for hvert barn (i) i barn
            forelder_map[i] = forelder #setter forelder_map med abrnet som nokkel og forelder som verdi
            #Dette sikrer at alle barn som grener til samme forelder har denne forelder som verdi
            #Det betyr videre at uansett hvilken av barna katten staar paa saa kan den naa forelderen
    
    sti = [katt_start] #lager en liste, kalt sti, der kattens start er forste element
    current = katt_start #Setter kattens start som current posisjon

    while current in forelder_map: #Saa lenge current finnes i ordboka
        verdi = forelder_map[current] #henter forelderen til current fra forelder_map
        sti.append(verdi) #legger til verdien i lista (sti)
        current = verdi #Endrer current til aa peke paa verdien. Eller der katten naa sitter

    print(" ".join(map(str, sti))) #Printer ut stien med .join saa den ikke printes ut som en liste

if __name__ == "__main__":
    main()

#Hvordan kjore koden:
#Kjores fra cmd og input pastes/skrives inn 