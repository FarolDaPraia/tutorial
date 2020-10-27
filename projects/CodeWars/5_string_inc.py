# codewars 5 kyu - String incrementer
'''Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''


def increment(word):
    number = []
    for letter in word[::-1]:
        if letter.isnumeric():
            number.append(letter)
        else:
            break
    if not number:
        return word + '1'
    else:
        number.reverse()
        dig = int(''.join(number)) + 1
        temp = len(word) - len(number)
        slice_word = word[:temp]
        return slice_word + str(dig).zfill(len(number))


'''CodeWars Solution:
def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
'''


print(increment('foo'))
print(increment('foo23'))
print(increment('0042'))
print(increment('09'))
print(increment('foo001'))
print(increment('foo00'))
print(increment('foo100'))
print(
    increment('XfZ{*=Qz6223277273011185565679023644880826440000000008733984')
)
