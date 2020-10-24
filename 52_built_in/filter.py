letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']


def filterVowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if letter in vowels:
        return True
    else:
        return False


filteredVowels = filter(filterVowels, letters)
print(id(filteredVowels))
list_filteredVowels = list(
    filteredVowels
)  # if I don´t run this line, I can print each filterVowels


print('The filtered vowels are:')
for vowel in filteredVowels:
    print(vowel)

print(id(filteredVowels))


# print(f'Size of variable as list {list_filteredVowels.__sizeof__()}')
# print(f'Size of variable as filter {filteredVowels.__sizeof__()}')
# print(filteredVowels)
#
# print(f'Size of variable as filter {filteredVowels.__sizeof__()}')
# for vowel in filteredVowels:
#     print(vowel)
#
#
# # 2th example
# creature_names = ['Sammy', 'Ashley', 'Jo', 'Olly', 'Jackie', 'Charlie']
# print(list(filter(lambda x: x[0].lower() in 'aeiou', creature_names)))
