print("Welcome to my quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("NICE! Let's play :)")
score = 0

# Question 1(MCQ)
answer = input("Q1.How many bits does IPV4 have?\nA. 64\nB. 128\nC. 144\nD. 255 ")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 2(MCQ)
print("Q2.How many bits does IPV6 have? ")
print("A. 62")
print("B. 128")
print("C. 142")
print("D. 252")

answer = input()
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect")

# Question 3
answer = input("Q3.What does CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')

# Question 4
answer = input("Q4.What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print('Incorrect!')


# Question 5
answer = input("Q5.What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

# Result
print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
