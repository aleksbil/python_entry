#scprit was written to cover boredom during a lecture
lecture_total = int(input('How long is that lecture? (in minutes): '))
time_passed = 0
while time_passed < lecture_total:
    progress = int(input('How many minutes you just survived? '))
    time_passed += progress
    boredom_lvl = min(100, round((time_passed / lecture_total) * 100))
    print(f"You survived {time_passed}/{lecture_total} min. Your boredom lvl: {boredom_lvl}%")
    
    if boredom_lvl >= 100:
        print("Damn, you actually did it.")
        break 
    elif boredom_lvl > 50:
        print("Half way there.")
    else:
        print("Just started, can't give up yet!")

print("--- DONE---")





     