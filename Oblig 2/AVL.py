import sys

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.height = 0

class AVLTree():
    def __init__(self):
        self.root = None
        self.size_counter = 0
    
    #Lager en metode som regner ut hoyden til en node
    #Hoyden er den "lengste" stien ned til en lov (der det ikke lengre er barn)
    def height(self, v): 
        if v == None:
            return 0
        return v.height
    
    #Denne metoden balanserer treet, og er viktig for rotasjonene som skal skje
    #Balance factor er differansen mellom venstre og hoyre side (v.left - h.left)
    #Verdier som ligger utenfor -1, 0, 1 er ikke godtatt og treet er ikke lengre balansert
    def balance(self, v):
        if v == None:
            return 0
        return self.height(v.left) - self.height(v.right)

    
    def find_min(self, v): #Lager en metode som returnerer det minste elementet
        while v.left:
            v = v.left
        return v
        
    def contains(self, set, x):
        if set == None: #Sjekker om settet er tomt
            return False
        
        if set.value == x: #Sjekker om plassen vi staar paa i settet er X
            return True
        elif set.value < x: #Sjekker om plassen vi staar paa er mindre enn X
            if set.right == None: #Om det ikke finnes noe hoyre nabo saa finnes ikke X i settet
                return False
            else:
                return self.contains(set.right, x) #Returnerer et kall paa funksjonen med hoyre nabo
        else:
            if set.left == None: #Sjekker om vi har noe venstre nabo
                return False
            return self.contains(set.left, x) #Returnerer et kall paa funksjonen med venstre nabo



    def insert(self, set, x):
        if set == None: #Sjekeker om settet er tomt
            self.size_counter += 1
            return Node(x) #Returnerer en ny Node om treet er tomt

        if set.value == x: #Sjekker om verdien eksisterer allerede
            return set
        
        if x < set.value:
            set.left = self.insert(set.left, x) #Om verdien vi setter inn er mindre enn plassen vi staar, gaar vi til venstre
        else:
            set.right = self.insert(set.right, x) #Ellers gaar vi til hoyre

        set.height = 1 + max(self.height(set.left), self.height(set.right)) #Setter hoyden til 1 + den hoyeste verdien av hoyre og venstre 
        balance = self.balance(set) #Balanserer settet

        #Venstre rotasjon
        if balance > 1 and self.value < set.left.value: #Om balansen er storre enn 1, altsaa naar treet er venstre-tungt, og verdien er mindre enn verdien til venstre
            return self.right_rotate(set) #Hoyre-rotasjon
        
        #Hoyre rotasjon
        if balance < -1 and self.value > set.right.value: #Om balansen er mindre enn -1, altsaa treet er hoyre-tungt, og verdien er storre enn verdien til hoyre
            return self.left_rotate(set) #Venstre-rotasjon
        
        #Venstre-hoyre rotasjon
        if balance > 1 and self.value > set.left.value: #Om balansen er storre enn 1, venstre-tungt, og verdien er storre enn venstre verdien
            set.left = self.left_rotate(set.left) #Roterer forst venstre
            return self.right_rotate(set) #Deretter hoyre
        
        #Hoyre-venstre rotasjon
        if balance < -1 and self.value < set.right.value: #Om balansen er mindre enn -1, hoyre-tungt, og verdien er mindre enn hoyre verdi
            set.right = self.right_rotate(set.right) #Roterer hoyre
            return self.left_rotate(set) #Deretter venstre

        return set

    def remove(self, set, x):
        if set == None: #Hvis settet er tomt
            return None
        
        if x < set.value: #Om verdien er mindre enn plassen vi staar
            set.left = self.remove(set.left, x)#Gaa mot venstre
        elif x > set.value:#Samme logikk, bare mot hoyre
            set.right = self.remove(set.right, x)
        
        else: #Her er fjerningen
            #Noden har ett eller ingen barn
            if set.left == None:
                self.size_counter -= 1
                return set.right #Returnerer hoyre subtre
            elif set.right == None:
                self.size_counter -= 1
                return set.left #Returnerer venstre subtre
        
        #Noden har to barn
        if set.right:
            fjerne = self.find_min(set.right) #Finner den minste verdien i hoyre subtre. Altsaa den verdien som er minst, men som er storre enn roten
            set.value = fjerne.value #Erstatter verdien vi staar i med verdien som skal fjernes (det rekursive kallet over)
            set.right = self.remove(set.right, fjerne.value) #Fjerner verdien fra hoyre subtre

        set.height = 1 + max(self.height(set.left), self.height(set.right))
        balance = self.balance(set)

        #Venstre rotasjon
        if balance > 1 and self.value < set.left.value: #Om balansen er storre enn 1, altsaa naar treet er venstre-tungt, og verdien er mindre enn verdien til venstre
            return self.right_rotate(set) #Hoyre-rotasjon
        
        #Hoyre rotasjon
        if balance < -1 and self.value > set.right.value: #Om balansen er mindre enn -1, altsaa treet er hoyre-tungt, og verdien er storre enn verdien til hoyre
            return self.left_rotate(set) #Venstre-rotasjon
        
        #Venstre-hoyre rotasjon
        if balance > 1 and self.value > set.left.value: #Om balansen er storre enn 1, venstre-tungt, og verdien er storre enn venstre verdien
            set.left = self.left_rotate(set.left) #Roterer forst venstre
            return self.right_rotate(set) #Deretter hoyre
        
        #Hoyre-venstre rotasjon
        if balance < -1 and self.value < set.right.value: #Om balansen er mindre enn -1, hoyre-tungt, og verdien er mindre enn hoyre verdi
            set.right = self.right_rotate(set.right) #Roterer hoyre
            return self.left_rotate(set) #Deretter venstre
    
        return set
    
    #Rotasjoner er slik vi holder treet balansert. Et AVL tre kan ikke ha differanse paa hoyde mellom hoyre og venstre er i rangen [-1,0,1]
    #Om det ikke er det etter insert eller remove saa maa vi rotere
    def left_rotate(self, z): #Venstre rotasjon skjer naar vi er hoyre-tunge på treet
        y = z.right #Hoyre barn til z
        T1 = y.left #Venstre barn av y, som skal tilordnes en ny verdi
        y.left = z #Setter z som venstre barn av y
        z.right = T1 #Venstre subtre av y (T1) blir naa hoyre barn

        #Oppdaterer hoyden til nodene etter rotasjon
        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y #Blir naa ny rot 
    
    def right_rotate(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y
    
    #Siden denne burde ha O(1), saa tenker jeg at jeg kan ha en teller i insert og remove funksjonene.
    #Evt kunne man traversert treet for aa telle antall noder, men dette vil resultere i O(N)
    def size(self):
        return self.size_counter

#Kjøres i cmd
#antall kommandoer er forste input, saa operasjoner

def main():
    tree = AVLTree()
    n = int(input().strip())


    for _ in range(n):
        command = input().strip().split()
        if len(command) == 0:
            continue

        if command[0] == "insert":
            value = int(command[1])
            tree.root = tree.insert(tree.root, value)
        elif command[0] == "contains":
            value = int(command[1])
            if tree.contains(tree.root, value):
                sys.stdout.write("true\n")
                sys.stdout.flush()
            else:
                sys.stdout.write("false\n")
                sys.stdout.flush()
        elif command[0] == "remove":
            value = int(command[1])
            tree.root = tree.remove(tree.root, value)
        elif command[0] == "size":
            sys.stdout.write(f"{tree.size()}\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
    
#Kjores i cmd med paste av input

