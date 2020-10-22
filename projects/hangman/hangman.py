map_word = {}
blacklist = []


def guess(letter):
    global count
    index_word = []

    if letter in word:
        for index, element in enumerate(word):
            if letter is element:
                index_word.append(index)
                map_word[element] = index_word
        show()
    else:
        blacklist.append(letter)
        print(f"you have alread guessed wrong {blacklist}")
        show()
    fim()


def fim():
    if len(blacklist) != 6:
        pass
        if len(group_word) != len(map_word):
            letter = input("Please insert a letter: ")
            while letter in map_word or letter in blacklist:
                print(f"The letter {letter} would already inserted\n")
                letter = input("Please insert a new letter: ")
            return guess(letter)
        else:
            print("you´ve found the word!")
    else:
        print("you were hanged!")


def show():
    result = []
    for place in range(len(word)):
        result.append("_ ")
    for letter in map_word:
        places = map_word[letter]
        for place in places:
            result[place] = letter
    print(''.join(result))


print("please insert a word to be guessed:")
word = input("guessed word: ")
group_word = set(word)
print("\nlet's start the game.\n")
fim()
