import random

def deathsaves(attempts):
    stable = 0
    death = 0
    revive = 0
    
    for i in range(attempts):
        failure = 0
        success = 0
        while True:
            roll = random.randint(1, 20)
            if roll == 1:
                failure += 2
            elif roll == 20:
                revive += 1
                break
            elif roll >= 10:
                success += 1
            else:
                failure += 1
                
            if failure >= 3:
                death += 1
                break
            elif success >= 3:
                stable += 1
                break
    total = death + stable + revive
    print(death / total)
    print(stable / total)
    print(revive / total)

deathsaves(1000000)