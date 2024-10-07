# cmp (sammenligninger) og swaps (bytter) handteres automatisk av wrapper-klasser CountCompares og CountSwaps.
# Comparisons telles automatisk hver gang elementer sammenlignes, feks, while j >= 0 and liste[j] > value_to_sort
#Swaps telles hver gang .swap() kalles, feks naar vi bytter j med j+1

def sort(liste):
    n = len(liste)
    for i in range(1, n):
        value_to_sort = liste[i] #verdien vi vil plassere 
        j = i - 1
        #flytter elementer til hoyre saa vi har plass til value_to_sort
        while j >= 0 and liste[j] > value_to_sort:
            liste.swap(j, j + 1) #swap
            j -= 1
        #setter inn value_to_sort på rett plass
        liste[j + 1] = value_to_sort

    return liste



