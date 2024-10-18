import random
from words import word_list  # get words from another py file     
def get_word():
    word = random.choice(word_list)  # randomly select word from word_list
    return word.upper()  # convert word into upper case

def play(word):  # In this function define all the variables
    word_completion = "_"*len(word)  # no of balnks that words as word length 
    guessed = 0
    guessed_letter = []
    guessed_word = []
    tries = 6
    print("Let's play the game")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0: 
            # loop untill tries and guesing words become 0
            guess = input("Please guess a letter or word:").upper()
            if len(guess) == 1 and guess.isalpha():   # check guess input length is one letter and its a alphabet
                if guess in guessed_letter:
                     print("you already guess the letter",guess)
                elif guess not in word:
                     print(guess,"is not in the word")
                     tries -= 1
                     guessed_letter.append(guess)
                else:
                     print("Good job",guess,"is in the word")
                     guessed_letter.append(guess)
                     word_as_list = list(word_completion)
                     indices = [i for i,letter in enumerate(word) if letter == guess]
                     for index in indices:
                          word_as_list[index] = guess
                     word_completion = "".join(word_as_list)
                     if "_" not in word_completion: 
                          guess = True  
            

            elif len(guess) == len(word) and guess.isalpha():
                 if guess in guessed_word:
                      print("you already guessed the word",guess)
                 elif guess != word:
                      print(guess,"is not a word")
                 else:
                      guessed = True
                      word_completion = word
                 
            
            else:
                 print("Not a  valid guess")
            
            print(display_hangman(tries))
            print(word_completion)
            print("\n")
    if guessed:
        print("Congrats,you guessed the word! you win!")
    else:
        print("Sorry.you ran out of the tries.")
        print(f"Correct word is: {word}")
         
         
def display_hangman(tries):
    stages = [ """
                - - - - - - - -
                |              |
                |              O
                |             \\|/
                |              |
                |             / \\
                -
              """
              ,
              """
                - - - - - - - -
                |              |
                |              O
                |             \\|/
                |              |
                |             / 
                -
               """ 
               ,
               """
                 - - - - - - - -
                |              |
                |              O
                |             \\|/
                |              |
                |                
                -
                """ 
                ,
                """
                 - - - - - - - -
                |              |
                |              O
                |             \\|
                |              |
                |                
                -
                """ 
                ,
                """
                 - - - - - - - -
                |              |
                |              O
                |              |
                |              |
                |                
                -
                """ 
                ,
                """
                 - - - - - - - -
                |              |
                |              O
                |              
                |              
                |                
                -
                """ 
                ,
                """
                 - - - - - - - -
                |              |
                |              
                |              
                |              
                |                
                -
                """
    ] 
    return stages[tries]
def main():
     word = get_word()
     play(word)
     while input("play again?(Y/N)").upper() == "Y":
          word = get_word()
          play(word)
if __name__ == "__main__":
     main()

    
