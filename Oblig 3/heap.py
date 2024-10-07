# cmp (sammenligninger) og swaps (bytter) handteres automatisk av wrapper-klasser CountCompares og CountSwaps.
# Comparisons telles automatisk hver gang elementer sammenlignes, for eksempel naar liste[l] > liste[largest] 
# Swaps telles automatisk hver gang .swap() kalles

#lager metoder for aa hente ut venstre, hoyre og forelder
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def max_heapify(liste, heap_size, i):
    while True:
        l = left(i)
        r = right(i)
        largest = i

        #sjekker om venstre barn er storre enn roten
        if l < heap_size and liste[l] > liste[largest]:
            largest = l
        #sjekker om hoyre barn er storre enn det storste elementet
        if r < heap_size and liste[r] > liste[largest]:
            largest = r
        #Om det storste ikke er roten, swap og heapify
        if largest != i:
            liste.swap(i, largest) #bytter roten med det storste barnet
            i = largest
        else:
            break

def build_max_heap(liste):
    heap_size = len(liste)
    #Starter fraa den siste ikke-lov noden og heaper nodene 
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(liste, heap_size, i)

def sort(liste):
    build_max_heap(liste) #bygger max heap
    heap_size = len(liste)

    #henter ut det storste elementet og flytter det til slutten av listen
    for i in range(len(liste)-1, 0, -1):
        #flytter roten (storste element) til slutten
        liste.swap(0, i)
        heap_size -= 1
        max_heapify(liste, heap_size, 0) #heaper paa nytt


