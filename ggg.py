def display():
    for i in cross_word:
        for j in i:
            print(j, end=" ")
        print()


def PlaceHorizontal(i, j, word):
    for it in range(j, j+len(word)):
        cross_word[i][it] = word[it-j]


def PlaceVertical(i, j, word):
    for it in range(i, i+len(word)):
        cross_word[it][j] = word[it-i]


def RemoveHorizontal(i, j, word):
    if i > 0 and i < n-1:
        for it in range(j, j+len(word)):
            if (i-1 >= 0 and (cross_word[i-1][it] == "+" or cross_word[i-1][it] == "*")) and (i+1 <= n and (cross_word[i+1][it] == "+" or cross_word[i+1][it] == "*")):
                cross_word[i][it] = "+"
            else:
                continue
    elif i == 0:
        for it in range(j, j+len(word)):
            if (i+1 <= n and (cross_word[i+1][it] == "+" or cross_word[i+1][it] == "*")):
                cross_word[i][it] = "+"
            else:
                continue
    elif i == n-1:
        for it in range(j, j+len(word)):
            if (i-1 >= 0 and (cross_word[i-1][it] == "+" or cross_word[i-1][it] == "*")):
                cross_word[i][it] = "+"
            else:
                continue


def RemoveVertical(i, j, word):
    if j > 0 and j < n-1:
        for it in range(i, i+len(word)):
            if (j-1 >= 0 and (cross_word[it][j-1] == "+" or cross_word[it][j-1] == "*")) and (j+1 <= n and (cross_word[it][j+1] == "+" or cross_word[it][j+1] == "*")):
                cross_word[it][j] = "+"
            else:
                continue
    elif j == 0:
        for it in range(i, i+len(word)):
            if (j+1 <= n and (cross_word[it][j+1] == "+" or cross_word[it][j+1] == "*")):
                cross_word[it][j] = "+"
            else:
                continue
    elif j == n-1:
        for it in range(i, i+len(word)):
            if (j-1 >= 0 and (cross_word[it][j-1] == "+" or cross_word[it][j-1] == "*")):
                cross_word[it][j] = "+"
            else:
                continue


def CanPlaceHorizontal(i, j, word):
    if j + len(word) > n:
        return False
    if j - 1 >= 0 and cross_word[i][j-1] == "+":
        return False
    if j + len(word) < n and cross_word[i][j+len(word)] == "+":
        return False
    for it in range(j, j+len(word)):
        if cross_word[i][it] == '+':
            continue
        elif cross_word[i][it] == word[it-j]:
            continue
        else:
            return False
    return True


def CanPlaceVertical(i, j, word):
    if i + len(word) > n:
        return False
    if i - 1 >= 0 and cross_word[i-1][j] == "+":
        return False
    if i + len(word) < n and cross_word[i+len(word)][j] == "+":
        return False
    for it in range(i, i+len(word)):
        if cross_word[it][j] == '+':
            continue
        elif cross_word[it][j] == word[it-i]:
            continue
        else:
            return False
    return True


cross_word = [['*', '*', '+', '+', '+', '*', '*'], 
              ['*', '+', '+', '+', '+', '+', '+'], 
              ['+', '+', '+', '+', '+', '+', '+'], 
              ['+', '+', '+', '*', '+', '+', '+'], 
              ['+', '+', '+', '+', '+', '+', '+'], 
              ['+', '+', '+', '+', '+', '+', '*'], 
              ['*', '*', '+', '+', '+', '*', '*']]
words = ['ART', 'EMIT', 'FRATBOY', 'FRO', 'JOE', 'LUI', 'OUTLETS', 'PASS',
         'PHANTOM', 'POUCH', 'RON', 'SMOOTH', 'SUBJECT', 'THRUM', 'TROUPE', 'YES']
n = len(cross_word)
current = 1
solution = {}


def backtrack(word_index):
    if word_index == len(words):
        return True
    for i in range(n):
        for j in range(n):
            if CanPlaceHorizontal(i, j, words[word_index]):
                solution[(i, j, 'A')] = words[word_index]
                PlaceHorizontal(i, j, words[word_index])
                if backtrack(word_index+1):
                    return True
                solution.pop((i, j, 'A'))
                RemoveHorizontal(i, j, words[word_index])

            if CanPlaceVertical(i, j, words[word_index]):
                solution[(i, j, 'D')] = words[word_index]
                PlaceVertical(i, j, words[word_index])
                if backtrack(word_index+1):
                    return True
                solution.pop((i, j, 'D'))
                RemoveVertical(i, j, words[word_index])
    return False


if backtrack(0):
    count = 1
    for i in range(n):
        complete = False
        for j in range(n):
            if (i, j, 'A') in solution:
                print(str(count) + ',A,'+str(solution[(i, j, 'A')]))
                complete = True
            if (i, j, 'D') in solution:
                print(str(count) + ',D,'+str(solution[(i, j, 'D')]))
                complete = True
            if complete == True:
                count += 1
                complete = False
    # display()
else:
    print("Not Possible")
