import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
ans = random.choice(words)
n = 8
word = '-' * len(ans)
flag = False
while n != 0:  
    print(f"\n\n{word}")
    letter = input('Input a letter: > ')
    #print('\n')
    if letter in ans and letter not in word:
        temp = ''
        for i in range(len(ans)):
            if ans[i] != letter:
                temp = temp + word[i]
            else:
                temp = temp + letter
        word = temp
    elif letter in word:
        print("No improvements")
        n = n - 1
    else:
        print("No such letter in the word")
        n = n - 1
    
    if word == ans:
        flag = True
        break


if flag == True:
    print(f"{ans}\nYou guessed the word!\nYou survived!")
else:
    print("You are hanged!")




