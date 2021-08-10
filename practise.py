
def generate_rotations(list2):
    rotations = []
    for i in range(len(list2)):
        rotations.append(list2[i:]+list2[:i])
    return rotations

print(generate_rotations([3,1,2,0]))