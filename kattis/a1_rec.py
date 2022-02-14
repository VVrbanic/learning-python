from sys import exit

MAX_SIZE = 30

def make_paper(size):
	if size > MAX_SIZE: # toliko mali papir ne postoji - dakle ne mozemo napraviti
		print("impossible")
		exit()
	if papers[size] > 0: # ako imamo papir te velicine, uzmi ga i vrati 0
		papers[size] -= 1
		return 0
	else: # ako nemamo papir te velicine, vrati make_paper(size+1) + make_paper(size+1) + tape potreban da ih zalijepimo
		return make_paper(size+1) + make_paper(size+1) + sizes[size+1][1]

# generiraj velicine
sizes = { 2: (2**(-5/4), 2**(-3/4)) }
for i in range (3, MAX_SIZE+1):
    short, long = sizes[i-1]
    sizes[i] = (long / 2, short)

# napravi dictionary s brojem papira po velicinama
smallest_size = int(input())
papers_list = [int(e) for e in input().split()]
assert(smallest_size == len(papers_list) + 1)

papers = {size: papers_list[size-2] if (size-2) < len(papers_list) else 0 for size in range(2,MAX_SIZE+1)}
papers[1] = 0

# napravi a1 papir
tape = make_paper(1)
print(tape)