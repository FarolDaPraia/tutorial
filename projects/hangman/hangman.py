mapping_word = {}
blacklist = []


def guess_letter(letter):
    index_word = []

    if letter in word:
        for index, element in enumerate(word):
            if letter is element:
                index_word.append(index)
                mapping_word[element] = index_word
        show_status()
    else:
        blacklist.append(letter)
        print(f"you have alread guessed wrong {blacklist}")
        show_status()
    play()


def play():
    if len(blacklist) != 6:
        pass
        if len(group_word) != len(mapping_word):
            letter = input("Please insert a letter: ")
            while letter in mapping_word or letter in blacklist:
                print(f"The letter {letter} would already inserted\n")
                letter = input("Please insert a new letter: ")
            guess_letter(letter)
        else:
            print("you´ve found the word!")
    else:
        print("you were hanged!")


def show_status():
    result = []
    for place in range(len(word)):
        result.append("_ ")
    for letter in mapping_word:
        places = mapping_word[letter]
        for place in places:
            result[place] = letter
    print(''.join(result))


print("please insert a word to be guessed:")
word = input("guessed word: ")
group_word = set(word)
print("\nlet's start the game.\n")
print("\nyou can suggest only six wrong letter!\n")
play()
