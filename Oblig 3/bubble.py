# cmp (sammenligninger) og swaps (bytter) handteres automatisk av wrapper-klasser CountCompares og CountSwaps.
# Comparisons telles automatisk hver gang elementer sammenlignes, feks saa vil if liste[i] > liste[i+1] telles som en sammenligning 
# Swaps telles automatisk hver gang .swap() kalles
def sort(liste):
    n = len(liste) - 1 #indeks lengde
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, n): 
                if liste[i] > liste[i+1]: #Bobler opp
                    sorted = False
                    liste.swap(i, i + 1) #swap
        n -= 1 #Reduserer n med en siden det storste elementet er paa rett plass

    return liste

