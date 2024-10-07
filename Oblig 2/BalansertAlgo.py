
#OPPGAVE BYGGE BALANSERTE SOKETRAER a)
#Pseudo
#Input = en balansert arraylist - liste
#Output = en rekkefolge som sikrer et balansert binært soketre

#Procedure balansere(liste):
#   if liste = null then
#       return
#   midten = len(liste) / 2
#   print(midten)
#
#   balansere(liste[midten + 1:])
#   balansere(liste[:midten])


#Python kode av algoritmen
#Siden arrayet er sortert og uten duplikater:
def balansere(liste):
    if not liste: #Base-case
        return
    
    mid = len(liste) // 2 #Finner midten, som blir roten, eller noden med d = 0.
    print(liste[mid]) #Skriver ut midtpunktet

    balansere(liste[mid+1:]) #Balanserer hoyre siden, altsaa liste med indeks midten + 1 og ut listen
    #Her sended hoyre liste inn i et rekursivt kall
    balansere(liste[:mid]) #Balanserer venstre siden, altsaa liste med indeks 0 og hele veien til, men ikke inkl, midten

sortert_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
balansere(sortert_liste)

print("-----------------------------------------------------------")

#OPPGAVE BYGGE BALANSERTE SOKETRAER b)

import heapq

def heap(h):
    if len(h) == 0 or not h:  #Basecase
        return

    size = len(h)
    new_heap = []

    for _ in range(size//2):
        heapq.heappush(new_heap, heapq.heappop(h))
    
    mid = heapq.heappop(h)
    print(mid)

    heap(h)
    heap(new_heap)

sortert_liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapq.heapify(sortert_liste)
heap(sortert_liste)
