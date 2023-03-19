import random
import hangman_words
import hangman_art
correct_answer=random.choice(hangman_words.word_list)      
print(hangman_art.logo)

bottem_blank=[]
for i in range(0,len(correct_answer)):
    bottem_blank+="_"    
#將相同的字母填入
lives=6  
while lives!=0:
    guess_letter=input("Guess a letter:").lower()
    if guess_letter not in correct_answer:
        lives=lives-1
        print(hangman_art.stages[lives])
        if lives==0:
            print("You lose.")
    elif guess_letter in bottem_blank:
        lives=lives-1
        print(hangman_art.stages[lives])
        print("you have already guessed it")
        if lives==0:
            print("You lose.")
    else:
        for i in range(0,len(correct_answer)):
            letter=correct_answer[i]
            if letter==guess_letter:
                bottem_blank[i]=guess_letter
        if "_" not in bottem_blank:
            print("You win.")        
    print(bottem_blank)


    print(lives)