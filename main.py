import random

correct = 0
total = 0

length = int(input("How many questions? "))
for i in range(length):
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    correctans = num1 * num2
    userans = int(input(f"Question {i+1}\n{num1} x {num2} = "))

    total+=1
    if userans == correctans:
        print("Correct")
        correct+=1
    else:
        print("Incorrect")

    
print(f"{correct}/{total} questions answered correctly.")

input("Press ENTER to exit")
