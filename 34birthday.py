import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

match = 0

for i in range(trials):
    calender = []

    for j in range(days):
        calender.append(0)
    for k in range(people):
        birthday = random.randint(1, days)
        calender[birthday] += 1
        if birthday in calender:
            match += 1  
            break

print(match)
print(match/trials)