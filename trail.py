alphabets = "abcdefghijklmnopqrstuvwxyz"


def isPalin(string):
    if list(string) == list(string)[::-1]:
        return True
    else:
        return False


def is_vowel(char):
    if char in ["a", "e", "i", "o", "u"]:
        return True


def is_beauty_strings(string, n, count):
    if n == 0 and isPalin(string):
        count += 1
        return True
    for i in alphabets:
        if string != "" and is_vowel(string[len(string) - 1]) and is_vowel(i):
            continue
        string += i
        if is_beauty_strings(string, n - 1, count):
            count += 1
        string = str(list(string).pop())


n = 3
string = ""
is_beauty_strings(string, n, count=0)
print(count)