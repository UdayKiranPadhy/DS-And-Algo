"""

Given the string croakOfFrogs, which represents a combination of 
the string "croak" from different frogs, that is, multiple frogs 
can croak at the same time, so multiple “croak” are mixed. 
Return the minimum number of different frogs to finish all the 
croak in the given string.

A valid "croak" means a frog is printing 5 letters 
‘c’, ’r’, ’o’, ’a’, ’k’ sequentially. The frogs have to print all 
five letters to finish a croak. If the given string is not a 
combination of valid "croak" return -1.

Example 1:

Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.

Example 2:

Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:

Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.
Example 4:

Input: croakOfFrogs = "croakcroa"
Output: -1
 

Constraints:

1 <= croakOfFrogs.length <= 10^5
All characters in the string are: 'c', 'r', 'o', 'a' or 'k'.


"""


def minNumberOfFrogs(croakOfFrogs: str) -> int:
    current_frogs_croacking = 0
    maximum_no_of_frogs = 0
    for i in croakOfFrogs:
        if i == "c":
            current_frogs_croacking += 1
            maximum_no_of_frogs = max(maximum_no_of_frogs, current_frogs_croacking)
        elif i == "k":
            current_frogs_croacking -= 1

    if current_frogs_croacking == 0:
        return maximum_no_of_frogs
    else:
        return -1


# print(minNumberOfFrogs("croakcroa"))
# print(minNumberOfFrogs("croakcroak"))
# print(minNumberOfFrogs("crcoakroak"))
# print(minNumberOfFrogs("croakcrook"))  # Fails here because of croak is wrng croak.

# So we need to keep track of all the characters
def minNumberOfFrogs(croakOfFrogs: str) -> int:
    current_frogs_croacking = 0
    maximum_no_of_frogs = 0
    characters = {
        "c": 0,
        "r": 0,
        "o": 0,
        "a": 0,
        "k": 0,
    }
    for i in croakOfFrogs:
        if i not in characters:
            return -1
        if i == "c":
            current_frogs_croacking += 1
            characters[i] += 1
            maximum_no_of_frogs = max(maximum_no_of_frogs, current_frogs_croacking)
        elif i == "k":
            for i in "croa":
                characters[i] -= 1
            current_frogs_croacking -= 1
        else:
            characters[i] += 1

    if current_frogs_croacking == 0 and (list(characters.values()) == [0] * 5):
        return maximum_no_of_frogs
    else:
        return -1


# print("New mwthod")
print(minNumberOfFrogs("croakcroa"))
print(minNumberOfFrogs("croakcroak"))
print(minNumberOfFrogs("crcoakroak"))
print(minNumberOfFrogs("croakcrook"))


"""
Accepted one
"""


class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        if croakOfFrogs[0] != "c" or croakOfFrogs[-1] != "k":
            return -1
        current_frogs_croacking = 0
        maximum_no_of_frogs = 0
        characters = {
            "c": 0,
            "r": 0,
            "o": 0,
            "a": 0,
            "k": 0,
        }
        for i in croakOfFrogs:
            if i not in characters:
                return -1
            if i == "c":
                current_frogs_croacking += 1
                characters[i] += 1
                maximum_no_of_frogs = max(maximum_no_of_frogs, current_frogs_croacking)
            elif i == "k":
                for i in "croa":
                    characters[i] -= 1
                current_frogs_croacking -= 1
            else:
                characters[i] += 1

        if current_frogs_croacking == 0 and (list(characters.values()) == [0] * 5):
            return maximum_no_of_frogs
        else:
            return -1
