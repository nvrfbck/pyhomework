languages = ["Python", "Go", "Javascript", "PHP", "Perl", "Swift", "Flask"]
name = input("hey, whats your name: ")
print("we will play a game where you need to guess a word we have, you can only make 3 mistakes")
tries = 3
while tries > 0:
    print("tries left: ", tries)
    guess = input("tell me your guess: ")
    if guess in languages:
        print("you won!!!")
        break
    if any(guess in word.lower() for word in languages):
        print("you are close, there is something like that")
    else:
        tries = tries - 1
else:
    print("you lose")

