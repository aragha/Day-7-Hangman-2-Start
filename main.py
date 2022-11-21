import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = word_list[random.randint(0, len(word_list)-1)]
print("Chosen word is: " + chosen_word)

cwl = list(chosen_word)
display = []
for ch in chosen_word:
  display.append('_')
graceattempts = 10
wordcompleted = False
while (graceattempts > 0 and not wordcompleted):
  if '_' in display:
    wordcompleted = False
    guess=input("Enter your guess: ").lower()
    correctguess = False    
    for i in range(0, len(cwl)):
        if cwl[i] == guess:
          display[i] = guess
          correctguess = True
    graceattempts -= 1
    print(display)  
    print(f"Attempts left: {graceattempts}")
    print("-----------------")
  else:
    wordcompleted = True
if wordcompleted:
  print(f"You win! You guessed the word {chosen_word} ")
else:
  print(f"You lose! The word was {chosen_word} ")