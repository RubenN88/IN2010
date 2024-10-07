import sys

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size_counter = 0
    
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
    
        return set
    
    #Siden denne burde ha O(1), saa tenker jeg at jeg kan ha en teller i insert og remove funksjonene.
    #Evt kunne man traversert treet for aa telle antall noder, men dette vil resultere i O(N)
    def size(self):
        return self.size_counter
    
#Kjores i CMD

def main():
    tree = BinarySearchTree()
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