import random

genome_size = 1000
genome = []
read_length = 10
read_count = 5
genome = [0]* genome_size
print(genome)

for i in range(read_length):
    read = random.randint(0,read_count)
    genome.append(read)