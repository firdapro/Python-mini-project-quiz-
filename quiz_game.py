print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Nice! let's play ;)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1  

else:
    print('Incorrect!')

answer = input("Who is the current flame Hashira? ")
if answer.lower() == "rengoku":
    print('Correct!')  
    score += 1

else:
    print('Incorrect!')

answer = input("Who is the current insect Hashira?  ")
if answer.lower() == "shinobu":
    print('Correct!')  
    score += 1

else:
    print('Incorrect!')

answer = input("What is a RAM  ")
if answer.lower() == "random access memory":
    print('Correct!')  
    score += 1

else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%." )

print("You got" + str((score/4)*100) + "%." )