# Create a introduction function and welcome the player by printing the statement of welcome.

def introduction():
    print("WELCOME TO HANGMAN!")
    print("\n", end=" ")
    # Making sure the player knows the rules by printing the rules
    print("Rules")
    print("You have 6 attempts only to guess the word")
    print("You can opt for a hint by typing hint")
    print("You can only type in 1 letter at a time")
    print("You will get your score at the end of the game")


word = ""


def choose_word():
    print("Enter any number from 1 to 9")
    n = int(input())
    # Ask for input (a number from 1-9) with the help of the input function and then returning the respective word.
    # Saving the appropriate word in the variable word, so when a player chooses a number, they receive a short description and the number of letters the word has.
    if n > 9 or n <= 0:
        print("Invalid number, please try again")
        choose_word()
    if n > 0 and n <= 9:
        global word
        if n == 1:
            print("A HUMAN ORGAN")
            word = "PANCREAS"
        if n == 2:
            print("A COUNTRY")
            word = "UZBEKISTAN"
        if n == 3:
            print("A THING")
            word = "DICTIONARY"
        if n == 4:
            print("A COLOUR")
            word = "MAGENTA"
        if n == 5:
            print("A SPORT")
            word = "SKATEBOARDING"
        if n == 6:
            print("A CITY")
            word = "MANCHESTER"
        if n == 7:
            print("A MOVIE")
            word = "INTERSTELLAR"
        if n == 8:
            print("AN ANIMAL")
            word = "RATTLESNAKE"
        if n == 9:
            print("A CAR MANUFACTURE")
            word = "LAMBORGHINI"
    return word

# If the player calls for a hint and types hint, the player will receive the hint for the word. For this purpose we create another helper function.


def hint(word):
    if word == "PANCREAS":
        print("Helps in digestive process.")
    if word == "UZBEKISTAN":
        print("A country in Central Asia and former member of Soviet Union.")
    if word == "DICTIONARY":
        print("Helps in knowing the meanings")
    if word == "MAGENTA":
        print("A purplish shade")
    if word == "SKATEBOARDING":
        print(
            "A sport invloving riding and performing tricks, yet to be included in Olympics")
    if word == "MANCHESTER":
        print("A city in UK")
    if word == "INSTERSTELLAR":
        print("Murphy's Theory")
    if word == "RATTLESNAKE":
        print("A venomous snake")
    if word == "LAMBORGHINI":
        print("An itialian brand famous for sports car")


# We created a dictionary and keys of the key will correspound to the tries, while the values of the keys will give us avisual representation.
# We have used three inverted commas so we can represent the value of dictionary in multi lines.
dic = {0: """
            _ _ _
                |
                o
               \|/
                |
               / \\
        """,
       1: """
            _ _ _
                |
                o
               \|/
                |
               / 
        """,
       2: """
            _ _ _
                |
                o
               \|/
                |
               
        """,
       3: """
            _ _ _
                |
                o
               \|
                |
               
        """,
       4: """
            _ _ _
                |
                o
                |
                |
               
        """,
       5: """
            _ _ _
                |
                o
              
                  
            
        """,
       6: """
            _ _ _
                |
               
              
               
             
        """, }


def function():
    introduction()
    global dic
    print(dic[6])
    word = choose_word()
    # To make sure the player knows the length of the word, the group members multiplied a dash (-) to the length of the word (_ * len(word)).
    word_blanks = "_"*len(word)
    print(word_blanks)
    # We created a list of guessed letters so a guess cannot repeat and user can play the game easily.
    guessed_letters = []
    tries = 6
    # We ran a while loop to ensure that the total number of tries the player has is 6, and until the tries are greater than zero, the while loop will keep functioning.
    while tries > 0:
        guess = input("Please guess a letter: ").upper()
        # If the guess is hint, then a hint would be printed to help the user.
        if guess == "HINT":
            hint(word)
        # we first had to make sure that the player could only guess one letter at a time so we coded that if the length of the guess is not equal to one or hint, print an error message.
        if len(guess) != 1 and guess != "HINT":
            print("Enter only one letter")
        if len(guess) == 1 and guess.isalpha():
            # This will check if the letter is guessed or not. If it is guessed then it will print the letter is already guessed.
            if guess in guessed_letters:
                print("You already guessed the letter")
            # If the guess is not in word, the tries will reduce by 1 and it will print that the letter is incorrect
            if guess not in word:
                print("The letter is incorrect")
                guessed_letters.append(guess)
                tries = tries-1
                print(dic[tries])
                if tries != 1:
                    print("You have", tries, "tries left")
                # If only one try is left it will give a warning to the user.
                if tries == 1:
                    print("Last chance!. You only have 1 attempt left.")
            # If the guess is correct, it will print the statement that the guess is correct.
            if guess not in guessed_letters and guess in word:
                guessed_letters.append(guess)
                print("Good job", guess, "is correct guess")
                # It will check the position of gussed letter by converting it into list and using enumerate function.(new method used).
                word_list = list(word_blanks)
                # Index_list will give us a list of all indexs where our guessed letter is present.
                index_list = [x for x, letter in enumerate(
                    word) if letter == guess]
                # By using index_list, we will return the letter to their appropriate position.
                for i in index_list:
                    word_list[i] = guess
                # We break the list and convert it back to string and print it.
                word_blanks = "".join(word_list)
                print(word_blanks)
                if "_" not in word_blanks:
                    # If the word is guessed it will print Congratulations.
                    print("Congratulations, You won!")
                    # The score will be calculated from tries left and the score would be printed.
                    score = (tries/6)*100
                    score = round(score)
                    print("Your score was", score)
                    break
    # When the player has made enough wrong guesses and the number of tries is equal to zero, the game ends.
    if tries == 0:
        print("Sorry you lost. The word was", word, ".")
        print("Your score was 0")


def main():
    function()
    # In the end, we ask the player if he/she wants to play the game again, if the answer is yes, the code takes them back to the start. Else if the answer is no, the game ends finally.
    while True:
        print("Do you want to play again, Yes or No")
        play_again = input().lower()
        if play_again == "yes":
            function()
        if play_again == "no":
            print("Thankyou for playing with us. Come back again.")
            break


main()
