import random 

# pick random word
word_list = ["cloud", "heart", "brake", "funny", "local", "penny", "strap", "paper", "pokes", "chair", "table", "pinky"]
hidden_word = random.choice (word_list)

print("This is wordle! guess a word thats 5 letters and ill tell you if you are close.🟩 means correct and in the right place,🟨 means its correct but in the wrong place, ⬛ means its not in the word.")
#repeat 6 guesses
for i in range (6):
    guess_word = input()
    output = ""

    #first letter
    if guess_word [0] == hidden_word[0]:
        output+= "🟩"
    elif guess_word [0] in hidden_word:
        output += "🟨"
    elif guess_word.isdigit():
        output += "Please enter a valid word."

    else:
        output += "⬛"

    if guess_word [1] == hidden_word[1]:
        output+= "🟩"
    elif guess_word [1] in hidden_word:
        output += "🟨"
    elif guess_word.isdigit():
        output += ""
    else:
        output += "⬛"

    if guess_word [2] == hidden_word[2]:
        output+= "🟩"
    elif guess_word [2] in hidden_word:
        output += "🟨"
    elif guess_word.isdigit():
        output += ""
    else:
        output += "⬛"
    
    if guess_word [3] == hidden_word[3]:
        output+= "🟩"
    elif guess_word [3] in hidden_word:
        output += "🟨"
    elif guess_word.isdigit():
        output += ""
    else:
        output += "⬛"

    if guess_word [4] == hidden_word[4]:
        output+= "🟩"
    elif guess_word [4] in hidden_word:
        output += "🟨"
    elif guess_word.isdigit():
        output += ""
    else:
        output += "⬛"

    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You Win!")
        break
    