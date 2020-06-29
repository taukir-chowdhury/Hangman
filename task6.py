import random
while True:
    print("H A N G M A N")
    x = input(f"Type \"play\" to play the game, \"exit\" to quit: >")
    if x == 'exit':
        quit()
    words = ['python', 'java', 'kotlin', 'javascript']
    ans = random.choice(words)
    n = 8
    word = '-' * len(ans)
    flag = False
    typed_letter = []

    while n != 0:  
        print(f"\n\n{word}")
        letter = input('Input a letter: >')
    
        if len(letter) != 1:
            print("You should input a single letter")
            continue
        if letter.islower() == False:
            print('It is not an ASCII lowercase letter')
            continue
        if letter in typed_letter:
            print("You already typed this letter")
            continue
    
        typed_letter.append(letter)
        if letter in ans and letter not in word:
            temp = ''
            for i in range(len(ans)):
                if ans[i] != letter:
                    temp = temp + word[i]
                else:
                    temp = temp + letter
            word = temp
    
       
        else:
            print("No such letter in the word")
            n = n - 1
    
        if word == ans:
            flag = True
            break


    if flag == True:
        print(f"You guessed the word {ans}!\nYou survived!")
    else:
        print("You are hanged!")
















