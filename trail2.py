def isPalin(string):
    if list(string) == list(string)[::-1]:
        return True
    else:
        return False


print(isPalin("bac"))