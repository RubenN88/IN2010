import sort_runner
import sys

def main(filename):
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]
    sort_runner.run_algs_part1(A, filename)
    sort_runner.run_algs_part2(A, filename)

if __name__ == '__main__':
    main(sys.argv[1])

#Hvordan kjore koden:
#Kjores fra cmd og input tas inn som et filnavn 
#feks: C:\riktig\sti\til\programmet>python main.py nearly_sorted_10.txt