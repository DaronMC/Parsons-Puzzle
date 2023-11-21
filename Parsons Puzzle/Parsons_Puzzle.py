import random
rd = random.randint(1,9)
guess = 0
c = 1
while guess != rd and guess != "exit":
    guess = int( input("Enter a guess between 1 to 9") )
    if guess == rd:
        print("Right!")
        print("You took only", c, "tries!")
    elif guess > rd:
        print("Too high")
        c += 1
    else:
        print("Too low")
        c += 1