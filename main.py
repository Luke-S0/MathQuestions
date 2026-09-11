import random
import time

version = "0.2.0"
correct = 0
total = 0

log = [] # 2d array - 0 question, 1 userans, 2 correctans, 3 result (bool)
length = int(input("How many questions? "))
for i in range(length):
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    correctans = num1 * num2
    userans = int(input(f"Question {i+1}\n{num1} x {num2} = "))

    total+=1
    if userans == correctans:
        print("Correct")
        log.append([f"{num1} * {num2}", userans, correctans, True])
        correct+=1
    else:
        print("Incorrect")
        log.append([f"{num1} * {num2}", userans, correctans, False])


print("OVERVIEW")
for i in range(0, len(log)):
    print(f"Question {i+1} : {log[i][0]}\nYou answered {log[i][1]}; correct answer was {log[i][2]}\nCorrect? {log[i][3]}")
    print("-"*50)
    time.sleep(1)

print(f"{correct}/{total} questions answered correctly.")

input("Press ENTER to exit")
