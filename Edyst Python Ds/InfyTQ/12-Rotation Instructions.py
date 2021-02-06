"""
You are given a string, in the format:

string:num1:num2:num3
The string can contain characters, specials characters and also numbers. num1, num2 and num3 are instructions to rotate the string.

You have to rotate the string to the right side by num1 positions
then rotate the string to the left side by num2 positions
finally, remove all the elements that are present at the indexes that are a multiple of num3
Example Input

hello1welcome2@python:5:2:3
Output

onelo1elom2@yt
"""
def rightrotate(string):
    return string[-1]+string[:-1]

def leftrotate(string):
    return string[1:]+string[0]

k=input().split(":")
string=k[0]
for i in range(int(k[1])):
    string=rightrotate(string)
for i in range(int(k[2])):
    string=leftrotate(string)
l=list(string)
step=int(k[3])-1
if step !=0:
    for i in range(0,len(l),int(k[3])-1):
        try:
            del l[i]
        except:
            continue
    print("".join([str(i) for i in l]))
else:
    print("")