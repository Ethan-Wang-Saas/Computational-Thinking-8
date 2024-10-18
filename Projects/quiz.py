#beginning 
import sys
answered = 0
lives = 3
points = 0


#middle
answer = input("What is 1+1?")
if answer == "2":
    points += 1
    answered += 1
else:
    lives -= 1
    answered += 1

print("")
answer = input("Which is better, Soccer(A) or Basketball(B)")
if answer == "A":
    lives -= 1
    answered += 1
elif answer == "B":
    points += 1
    answered += 1

print("")
answer = input("What is the capitol of Washington State, Seattle(A), or Olympia(B)?")
if answer == "A":
    lives -= 1
    answered += 1
elif answer == "B":
    points += 1
    answered += 1

if lives == 0:
    print("")
    print("You ran out of lives...")
    sys.exit()

print("")
answer = input("What is the largest ocean on the earth, Pacific(A), or Atlantic(B)?")
if answer == "A":
    points += 1
    answered += 1
elif answer == "B":
    lives -= 1
    answered += 1

if lives == 0:
    print("")
    print("You ran out of lives...")
    sys.exit()

print("")
answer = input("What is the smallest country in the world, Monaco(A), or Vatican City(B)?")
if answer == "A":
    lives -= 1
    answered += 1
elif answer == "B":
    points += 1
    answered += 1

if lives == 0:
    print("")
    print("You ran out of lives...")
    sys.exit()

#end
print("")
if points == 5:
    print("You got all of them right and lost no lives!")
elif points == 4:
    print("You got one question wrong, but you won!")
elif points == 3:
    print("You were one question away from losing, but you won.")