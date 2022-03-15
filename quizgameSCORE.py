#define score

score = 0
questions = 20

#Quiz game
print("Welcome to the dungeon!")

playing = input("Ready to play? yes/no ")
print("remember no capital letters in your answers!")
print(playing)

if playing != "yes":
    quit()

print("Goodluck Peasant! ")

#1

answer = input("What does VR stand for? ")
if answer == "virtual reality":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#2

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct moving on!")
    score+=1
else:
    print("incorrect, try again!")
    

#3

answer = input("How many primary colors are there? ")
if answer == "3":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#4

answer = input("Who discovered gravity? ")
if answer == "issac newton":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#5

answer = input("When did the first Iphone come out? ")
if answer == "2007":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#6

answer = input("When was Telsa founded? ")
if answer == "2003":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#7

answer = input("How many questions did you just answer? ")
if answer == "6":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#8

answer = input("what year did the first person stand on the moon? ")
if answer == "1969":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#9

answer = input("who was the second person to land on the moon? ")
if answer == "buzz aldrin":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#10

answer = input("How many days does it take for the Earth to orbit the Sun? ")
if answer == "365.25":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#11

answer = input("how many time zones are in russia? ")
if answer == "11":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#12

answer = input("what is the capital of russia? ")
if answer == "moscow":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#13

answer = input("which language has the most words? ")
if answer == "english":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#14

answer = input("what is 9 x 5 + 24? ")
if answer == "69":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#15

answer = input("what country has the most islands in the world? ")
if answer == "sweden":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#16

answer = input("what country has the highest population? ")
if answer == "china":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#17

answer = input("what is the smallest country? (it's also a city) ")
if answer == "vatican city":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#18

answer = input("what country has the highest crime rate? ")
if answer == "venezuela":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#19

answer = input("what is the most sold video game? ")
if answer == "minecraft":
    print("Correct moving on!")
    score +=1 
else:
    print("incorrect, try again!")
    

#20

answer = input("what is the most used coding language? (by 80% of developers) ")
if answer == "python":
    print("you have completed my quiz, you are very smart!")
    score +=1 
else:
    print("incorrect on the last question!")

print(f"your score was {score} out of 20 questions! goodjob!")
    
