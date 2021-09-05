def output(n):
    if n > 10:
        tens_place = generate(str(n)[0], False)
        ones_place = generate(str(n)[1])
        return tens_place + ones_place
    else:
        tens_place = [0, 0, 0, 0, 0]
        ones_place = generate(str(n)[0])
        return tens_place + ones_place


def generate(string1, ones_place=True):
    number = int(string1)
    to_return = [0, 0, 0, 0, 0]
    if ones_place:
        if number >= 5:
            to_return[0] = 1
            number -= 5
        pointer = 4
        while number != 0:
            to_return[pointer] = 1
            pointer -= 1
            number -= 1
        return to_return
    else:
        if number >= 5:
            to_return[4] = 1
            number -= 5
        pointer = 0
        while number != 0:
            to_return[pointer] = 1
            pointer += 1
            number -= 1
        return to_return


n = int(input())
print(*output(n))
