import random
print("H A N G M A N")
words = ['python', 'java', 'kotlin', 'javascript']
ans = random.choice(words)
ans2 = ans[3:]
blank = '-' * len(ans2)
print(f'{ans[:3]}{blank}')
word = input('Guess the word: > ')
if word == ans:
    print("You survived!")
else:
    print("You are hanged!")