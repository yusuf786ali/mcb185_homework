import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0

for i in range(trials):
    birthdays = [] 

    for j in range(people):
        birthday = random.randint(1, days)
        if birthday in birthdays:
            match += 1  
            break
        birthdays.append(birthday)

print(match)
print(match/trials)