# cmp (sammenligninger) og swaps (bytter) handteres automatisk av wrapper-klasser CountCompares og CountSwaps.
# Comparisons telles automatisk hver gang elementer sammenlignes, feks naar if venstre_subliste[i] <= hoyre_subliste[j]
# Swaps telles automatisk hver gang .swap() kalles naaar vi bytter plass paa noe fra hoyre subliste og settes foran elementet i venstre subliste

def sort(liste):
    merge_sort(liste, 0, len(liste) - 1)
    return liste

def merge_sort(liste, venstre, hoyre):
    #Base case
    if venstre > hoyre:
        return
    #fortsetter splitting frem til venstre indeks er mindre enn hoyre
    if venstre < hoyre:
        mid = (venstre + hoyre) // 2 #Finner midten
        merge_sort(liste, venstre, mid) #rekursivt kall paa forste halvdel
        merge_sort(liste, mid + 1, hoyre) #rekursivt kall paa andre halvdel
        merge(liste, venstre, mid, hoyre) #setter de to sammen

def merge(liste, venstre, mid, hoyre):
    #merger to sorterte lister til en sortert liste
    venstre_subliste = liste[venstre:mid+1]
    hoyre_subliste = liste[mid+1:hoyre+1]
    i = 0 #indeks for forste liste
    j = 0 #indeks for andre liste
    k = venstre #indeks for det som skal merges

    #traverserer begge sublister og for hver iterasjon legger til det minste fra begge sublister
    while i < len(venstre_subliste) and j < len(hoyre_subliste):
        if venstre_subliste[i] <= hoyre_subliste[j]:
            liste[k] = venstre_subliste[i] #flytter fra venstre subtre
            #ingen swaps her da venstre subliste allerede er i riktig rekkefolge
            i += 1
        else:
            liste[k] = hoyre_subliste[j] #flytter fra hoyre subliste
            liste.swap(k,j) #teller dette som en swap da vi flytter element fra hoyre og setter det forran det fra venstre
            j += 1
        k += 1
    #kopierer venstre og hoyre subliste sammen, ingen swaps her
    while i < len(venstre_subliste):
        liste[k] = venstre_subliste[i]
        i += 1
        k += 1

    while j < len(hoyre_subliste):
        liste[k] = hoyre_subliste[j]
        j += 1
        k += 1
    return liste
