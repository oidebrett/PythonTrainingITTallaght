import random

n1 = random.randint(0,12)
n2 = random.randint(0,12)
ans = n1 * n2

print("%d * %d" %(n1,n2))

foundCorrectAnswer = False

while not foundCorrectAnswer:
    usrAns = int(input("Enter your answer: "))

    if usrAns == ans:
        print("Correct")
        foundCorrectAnswer = True
    elif usrAns>ans:
        print("Too high")
    elif usrAns<ans:
        print("Too low")


print("The correct answer was %d" %(n1*n2))
print("Goodbye")